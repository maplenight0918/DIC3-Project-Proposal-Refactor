"""Build the DIC3 refactor without overwriting any original proposal artifact.

Uses the existing requirements-docs.txt. The committed PNGs allow offline builds;
use --render-diagrams with MMDC set to a Mermaid CLI 11.12.0 executable to refresh.
"""
from pathlib import Path
import argparse, hashlib, html, json, os, re, subprocess, tempfile
import fitz
import markdown
from PIL import Image
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'deliverables/refactor'
ASSETS = ROOT / 'assets/refactor'
W, H = 960, 540
FONT = fitz.Font('cjk')
FONT_NAME = 'Droid Sans Fallback'


def normalized_section(text):
    return re.sub(r'^(#{1,5}) ', r'#\1 ', text, flags=re.M).strip()


def synced_proposal():
    path = ROOT / 'research/proposal_refactored.md'
    s = path.read_text()
    design = (ROOT / 'DESIGN.md').read_text().split('## Problem', 1)[1]
    design = '## Problem' + design
    # Design links originate at root; embedded section resides in research/.
    design = re.sub(r'\]\((?!https?:|#)([^)]+)\)', lambda m: '](' + '../' + m[1] + ')', design)
    evaluation = (ROOT / 'research/refactor/evaluation.md').read_text().split('\n', 1)[1]
    for tag, content in [('DESIGN', normalized_section(design)), ('EVALUATION', normalized_section(evaluation))]:
        s = re.sub(r'<!-- ' + tag + r'_BEGIN -->.*?<!-- ' + tag + r'_END -->',
                   lambda _: f'<!-- {tag}_BEGIN -->\n{content}\n<!-- {tag}_END -->', s, flags=re.S)
    path.write_text(s)
    return s


def diagram_sources():
    d = (ROOT / 'DESIGN.md').read_text()
    for name, block in zip(['architecture', 'flowchart'], re.findall(r'```mermaid\n(.*?)\n```', d, re.S)):
        (ASSETS / f'{name}.mmd').write_text(block + '\n')


def render_diagrams():
    mmdc = os.environ.get('MMDC', 'mmdc')
    with tempfile.TemporaryDirectory(prefix='energy-diagrams-') as td:
        td = Path(td)
        pp = {'args': ['--no-sandbox']}
        if os.environ.get('CHROME_BIN'):
            pp['executablePath'] = os.environ['CHROME_BIN']
        (td/'puppeteer.json').write_text(json.dumps(pp))
        (td/'mermaid.json').write_text(json.dumps({'theme':'neutral','fontFamily':FONT_NAME+', sans-serif',
            'flowchart':{'htmlLabels':False,'curve':'linear','nodeSpacing':26,'rankSpacing':38},
            'themeVariables':{'fontSize':'18px','primaryColor':'#e7f2f2','primaryTextColor':'#172d43','lineColor':'#087e8b'}}))
        for p in sorted(ASSETS.glob('*.mmd')):
            subprocess.run([mmdc,'-i',str(p),'-o',str(p.with_suffix('.png')),'-p',str(td/'puppeteer.json'),
                '-c',str(td/'mermaid.json'),'-w','1800','-s','2'],check=True)
    manifest = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in ASSETS.iterdir() if p.suffix in ('.png','.mmd')}
    (ASSETS/'diagram-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')


def write_html(s):
    names = iter(['architecture','flowchart'])
    s = re.sub(r'```mermaid\n.*?\n```', lambda _: f'![系統技術圖](../../assets/refactor/{next(names)}.png)',s,flags=re.S)
    # Resolve remaining relative links against the Markdown source directory.
    def links(m):
        target=m[1]
        if target.startswith(('http:', 'https:', '#')) or target.startswith('../../assets/refactor/'):
            return m[0]
        local=(ROOT/'research'/target).resolve()
        return ']('+os.path.relpath(local,OUT)+')'
    s=re.sub(r'\]\(([^)]+)\)',links,s)
    css='''body{font:17px/1.8 "Droid Sans Fallback",sans-serif;max-width:1160px;margin:36px auto;padding:0 28px;color:#172d43}h1,h2,h3{color:#087e8b}h2{margin-top:2em}table{width:100%;border-collapse:collapse;font-size:13px}th,td{border:1px solid #b9cbd1;padding:9px;vertical-align:top;overflow-wrap:anywhere}th{background:#e7f2f2}pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#eef3f6;padding:16px;font-size:12px}img{max-width:100%;height:auto}a{color:#006c7a}p{overflow-wrap:anywhere}@media print{body{font-size:10pt;margin:0}h2,h3{break-after:avoid}tr{break-inside:avoid}img{max-height:250mm;object-fit:contain}}'''
    body=markdown.markdown(s,extensions=['tables','fenced_code','toc'])
    (OUT/'Proposal.html').write_text('<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Energy Detective — DIC3 Proposal Refactor</title><style>'+css+'</style></head><body>'+body+'</body></html>')


def wrap(text, size, width):
    lines=[]
    for line in text.split('\n'):
        current=''
        for char in line:
            if current and FONT.text_length(current+char,fontsize=size)>width:
                lines.append(current);current=char
            else: current+=char
        lines.append(current)
    return lines


def build_slides():
    slides=json.loads((ROOT/'research/refactor/slides.json').read_text())
    # Technical algorithm always comes from the same source as the proposal.
    code=re.search(r'```text\n(.*?)\n```',(ROOT/'DESIGN.md').read_text(),re.S)[1].splitlines()
    codes=[code[:15],code[15:30],code[30:]]
    for s in slides:
        if s.get('code'):s['body']=codes.pop(0)
    prs=Presentation();prs.slide_width=Pt(W);prs.slide_height=Pt(H)
    pdf=fitz.open();deck_md=['# Energy Detective重構版Proposal逐頁稿\n\n所有產品能力為規劃，實驗待測。技術頁隨DESIGN重建；一般頁編輯research/refactor/slides.json。\n']
    layout=[]
    for i,s in enumerate(slides,1):
        slide=prs.slides.add_slide(prs.slide_layouts[6]);page=pdf.new_page(width=W,height=H)
        page.insert_font(fontname='cjkdoc',fontbuffer=FONT.buffer)
        page.draw_rect(page.rect,color=None,fill=(.96,.98,.99))
        bg=slide.background.fill;bg.solid();bg.fore_color.rgb=RGBColor.from_string('F5FAFC')
        boxes=[]
        def text(x,y,w,h,value,size=20,color='172D43',leading=None):
            leading=leading or size*1.28
            lines=wrap(value,size,w-8)
            needed=len(lines)*leading+4
            if needed>h: raise ValueError(f'Slide {i}: overflow {needed}>{h}: {value[:70]}')
            content='\n'.join(lines)
            tb=slide.shapes.add_textbox(Pt(x),Pt(y),Pt(w),Pt(h));tf=tb.text_frame
            tf.clear();tf.word_wrap=False
            tf.margin_left=Pt(4);tf.margin_right=Pt(4);tf.margin_top=Pt(1);tf.margin_bottom=Pt(0)
            for j,line in enumerate(lines):
                p=tf.paragraphs[0] if j==0 else tf.add_paragraph()
                p.text=line;p.font.name=FONT_NAME;p.font.size=Pt(size);p.font.color.rgb=RGBColor.from_string(color)
                p.space_before=Pt(0);p.space_after=Pt(0);p.line_spacing=Pt(leading)
                from pptx.oxml.xmlchemy import OxmlElement
                for run in p.runs:
                    ea=OxmlElement('a:ea');ea.set('typeface',FONT_NAME);run._r.get_or_add_rPr().append(ea)
            for j,line in enumerate(lines):
                page.insert_text((x+4,y+size+1+j*leading),line,fontname='cjkdoc',fontsize=size,color=tuple(int(color[k:k+2],16)/255 for k in (0,2,4)))
            boxes.append({'x':x,'y':y,'w':w,'h':h,'lines':len(lines),'font':size})
            return needed
        text(30,20,900,60,s['title'],28,'087E8B')
        if s.get('overview'):
            from pptx.enum.shapes import MSO_SHAPE
            labels=['① 需求解析\n與範圍驗證','② 受限規劃\n與工具控制','③ CSV取得\n與歷史重播','④ 時序資料\n品質檢查','⑤ 基準\n與異常分析','⑥ 領域規則\n與假說','⑦ 證據整合\n與報告','⑧ 離線評估']
            positions=[(34,104),(264,104),(494,104),(724,104),(724,290),(494,290),(264,290),(34,290)]
            for label,(x,y) in zip(labels,positions):
                rr=fitz.Rect(x,y,x+202,y+100)
                page.draw_rect(rr,color=(.03,.49,.55),fill=(.89,.95,.95),width=1.5)
                shape=slide.shapes.add_shape(MSO_SHAPE.RECTANGLE,Pt(x),Pt(y),Pt(202),Pt(100))
                shape.fill.solid();shape.fill.fore_color.rgb=RGBColor.from_string('E3F2F2')
                shape.line.color.rgb=RGBColor.from_string('087E8B')
                text(x+7,y+13,188,80,label,23)
            for x,y,arrow in [(238,135,'→'),(468,135,'→'),(698,135,'→'),(810,228,'↓'),(698,320,'←'),(468,320,'←'),(238,320,'←')]:
                text(x,y,32,45,arrow,24)
            text(34,215,745,61,'②依分析觀察選適用規則，或直接進⑦；\n⑧離線評估使用執行紀錄，不是在線控制設備。',18)
            text(34,418,890,62,'資料與品質／分析證據交給⑦；查核不足時補問或停止。\n完整含回饋與旁路的正式架構圖見Proposal §5與DESIGN.md。',18)
        if s.get('flow_native'):
            from pptx.enum.shapes import MSO_SHAPE
            from pptx.oxml.xmlchemy import OxmlElement
            def arrow(points,label=None,at=None):
                for aa,bb in zip(points,points[1:]):
                    page.draw_line(fitz.Point(*aa),fitz.Point(*bb),color=(.03,.49,.55),width=1.3)
                    line=slide.shapes.add_connector(1,Pt(aa[0]),Pt(aa[1]),Pt(bb[0]),Pt(bb[1]))
                    line.line.color.rgb=RGBColor.from_string('087E8B')
                aa,bb=points[-2:]
                import math
                dx,dy=bb[0]-aa[0],bb[1]-aa[1];length=math.hypot(dx,dy);ux,uy=dx/length,dy/length
                tri=[fitz.Point(*bb),fitz.Point(bb[0]-8*ux+4*uy,bb[1]-8*uy-4*ux),fitz.Point(bb[0]-8*ux-4*uy,bb[1]-8*uy+4*ux)]
                page.draw_polyline(tri,closePath=True,color=None,fill=(.03,.49,.55))
                tail=OxmlElement('a:tailEnd');tail.set('type','triangle');line._element.spPr.get_or_add_ln().append(tail)
                if label:text(at[0],at[1],200,43,label,13,'087E8B',leading=17)
            def node(x,y,w,h,label,decision=False):
                fill=(.90,.95,.95)
                if decision:
                    points=[fitz.Point(x+w/2,y),fitz.Point(x+w,y+h/2),fitz.Point(x+w/2,y+h),fitz.Point(x,y+h/2)]
                    page.draw_polyline(points,closePath=True,color=(.03,.49,.55),fill=fill)
                else:page.draw_rect(fitz.Rect(x,y,x+w,y+h),color=(.03,.49,.55),fill=fill)
                sh=slide.shapes.add_shape(MSO_SHAPE.DIAMOND if decision else MSO_SHAPE.ROUNDED_RECTANGLE,Pt(x),Pt(y),Pt(w),Pt(h))
                sh.fill.solid();sh.fill.fore_color.rgb=RGBColor.from_string('E6F2F2');sh.line.color.rgb=RGBColor.from_string('087E8B')
                margin=28 if decision else 8
                text(x+margin,y+11,w-margin*2,h-10,label,16 if decision else 18,leading=22)
            if s['flow_native']=='analysis':
                arrow([(285,132),(355,132)])
                arrow([(535,132),(650,132)],'否',(565,102))
                arrow([(445,174),(445,194),(155,194),(155,220)],'是',(320,170))
                arrow([(780,100),(780,82),(155,82),(155,105)],'是：同參數一次',(370,60))
                arrow([(780,168),(780,220)],'否',(795,182))
                arrow([(285,249),(355,249)])
                arrow([(285,240),(315,240),(315,207),(650,207),(650,236)],'工具錯誤',(440,181))
                arrow([(535,249),(605,249),(605,305),(650,305)],'不足',(570,268))
                arrow([(445,290),(445,318),(155,318),(155,342)],'足夠；缺天氣只停相關規則',(250,294))
                arrow([(285,369),(355,369)])
                arrow([(535,369),(615,369),(615,261),(650,261)],'否',(564,340))
                arrow([(445,410),(445,435),(285,435)],'是',(350,407))
                node(35,105,250,56,'③ 載入登錄CSV')
                node(355,90,180,84,'讀取成功？',True)
                node(650,100,270,68,'暫時I/O且未重試？\n否則不得重試')
                node(35,220,250,58,'④ 品質檢查')
                node(355,207,180,84,'用電／單位\n足夠？',True)
                node(650,220,270,58,'保存失敗／停止')
                node(650,285,270,58,'資料不足報告')
                node(35,342,250,58,'⑤ 固定切分與分析')
                node(355,327,180,84,'分析成功？',True)
                node(35,418,250,52,'接觀察決策階段')
            else:
                arrow([(285,137),(355,137)])
                arrow([(535,137),(650,137)],'是：選規則',(545,104))
                arrow([(445,178),(445,221)],'否',(458,187))
                arrow([(780,175),(780,230)])
                arrow([(535,146),(590,146),(590,257),(650,257)],'直接報告\n並記理由',(550,183))
                arrow([(780,286),(780,327)])
                arrow([(650,369),(550,369)],'否',(585,339))
                arrow([(355,369),(285,369)])
                arrow([(355,248),(155,248),(155,340)])
                arrow([(780,411),(780,433),(155,433),(155,400)],'是',(800,410))
                arrow([(155,400),(155,449)])
                node(35,110,250,58,'② 依分析觀察選擇')
                node(355,95,180,84,'選擇合法？',True)
                node(650,100,270,76,'⑥ 執行適用規則\n失敗記警告／保留分析')
                node(355,221,195,58,'既有證據／受限報告')
                node(650,230,270,58,'⑦ 產生報告')
                node(650,327,270,84,'成功且主張有效？',True)
                node(355,340,195,60,'本地固定模板')
                node(35,340,250,60,'保存報告／證據／紀錄')
                node(35,449,250,40,'⑧ 離線評估／結束')
        if s.get('diagram'):
            p=ASSETS/s['diagram'];im=Image.open(p)
            if s.get('full_diagram'):box=fitz.Rect(26,90,934,475)
            else:box=fitz.Rect(450,90,934,484)
            scale=min(box.width/im.width,box.height/im.height);iw,ih=im.width*scale,im.height*scale
            dest=fitz.Rect(box.x0+(box.width-iw)/2,box.y0+(box.height-ih)/2,box.x0+(box.width+iw)/2,box.y0+(box.height+ih)/2)
            page.insert_image(dest,filename=str(p));slide.shapes.add_picture(str(p),Pt(dest.x0),Pt(dest.y0),width=Pt(iw),height=Pt(ih))
        y=100
        if s.get('code'):
            for line in s['body']:
                used=text(30,y,900,25,line,11.5,leading=18);y+=max(23,used)
        else:
            width=395 if s.get('diagram') else 884
            for item in s['body']:
                value=item if i==1 else '• '+item
                used=text(34,y,width,105,value,20 if i==1 else 18.5)
                y+=used+14
                if y>486:raise ValueError(f'Slide {i} body extends to {y}')
        text(30,493,900,42,f'{i:02d}/{len(slides):02d}  ENERGY DETECTIVE | PROPOSAL REFACTOR\n'+s.get('source',''),10,'536579',leading=13)
        diagram_name = ('architecture' if s.get('overview') else
                        'flow-'+s['flow_native'] if s.get('flow_native') else
                        Path(s['diagram']).stem if s.get('diagram') else None)
        diagram_text = (ASSETS/(diagram_name+'.mmd')).read_text() if diagram_name else ''
        slide.notes_slide.notes_text_frame.text='\n'.join(s['body'])+'\n'+diagram_text+'\n'+s.get('source','')+'\n完整定義與來源：research/proposal_refactored.md；技術唯一來源：DESIGN.md。'
        deck_md.append(f'\n## {i:02d}. {s["title"]}\n\n'+'\n\n'.join(s['body'])+'\n\n'+s.get('source','')+'\n')
        if s.get('diagram'):deck_md.append(f'\n![{s["title"]}](../../assets/refactor/{s["diagram"]})\n')
        if diagram_text:
            deck_md.append('\n圖解逐頁稿（簡報採相同模組／分支的版面摘要；完整定義見DESIGN）：\n\n```mermaid\n'+diagram_text+'```\n')
        layout.append({'slide':i,'title':s['title'],'text_boxes':boxes})
    prs.save(OUT/'Proposal.pptx');pdf.subset_fonts();pdf.save(OUT/'Proposal-slides.pdf',garbage=4,deflate=True);pdf.close()
    (OUT/'slides.md').write_text('\n'.join(deck_md))
    (OUT/'slide-layout.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
    print(f'Created {len(slides)} editable PPTX slides, PDF preview and complete page text.')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--render-diagrams',action='store_true');args=ap.parse_args()
    OUT.mkdir(exist_ok=True,parents=True);ASSETS.mkdir(exist_ok=True,parents=True)
    diagram_sources()
    if args.render_diagrams:render_diagrams()
    elif (ASSETS/'diagram-manifest.json').exists():
        manifest=json.loads((ASSETS/'diagram-manifest.json').read_text())
        for name,digest in manifest.items():
            p=ASSETS/name
            if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:
                raise ValueError(f'{name} changed: rerun --render-diagrams before producing a stale diagram')
    else:raise ValueError('Missing diagram manifest; render diagrams first')
    s=synced_proposal();write_html(s);build_slides()
    print('Proposal technical sections synchronized from DESIGN and evaluation; original outputs untouched.')

if __name__=='__main__':main()
