"""Meaningful artifact checks for the refactor; does not run the future Agent."""
from pathlib import Path
import hashlib,json,re,zipfile,xml.etree.ElementTree as ET
from html.parser import HTMLParser
import fitz
from pptx import Presentation
from build_refactor import normalized_section

ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(ok,msg):
    if not ok: raise AssertionError(msg)
    checks.append(msg)

source=(ROOT/'research/proposal_refactored.md').read_text()
design=(ROOT/'DESIGN.md').read_text()
evaluation=(ROOT/'research/refactor/evaluation.md').read_text().split('\n',1)[1]
expected='## Problem'+design.split('## Problem',1)[1]
expected=re.sub(r'\]\((?!https?:|#)([^)]+)\)',lambda m:'](../'+m[1]+')',expected)
for tag,text in [('DESIGN',expected),('EVALUATION',evaluation)]:
    embedded=re.search(r'<!-- '+tag+r'_BEGIN -->\n(.*?)\n<!-- '+tag+r'_END -->',source,re.S)[1]
    check(embedded==normalized_section(text),tag+' generated section matches canonical source')
abstract=(ROOT/'research/refactor/abstract-zh.txt').read_text().strip()
count=len(re.sub(r'\s','',abstract))
check(abstract==re.search(r'<!-- ABSTRACT_ZH_BEGIN -->\n(.*?)\n<!-- ABSTRACT_ZH_END -->',source,re.S)[1],'Chinese abstract source matches proposal')
check(f'**{count}字**' in source and 280<=count<=320,f'Chinese abstract count {count} with stated counting rule')
for token in ['Attention Getter','But.','Cure.','Development.','Experiments.','Expected Outcomes.','Index Terms']:
    check(token in source,'Abstract coverage: '+token)
check(len(re.findall(r'^#### M[1-5] ',source,re.M))==5,'Five domain mindsets')
check(len(re.findall(r'^#### DQ[1-3] ',source,re.M))==3,'Three explicitly qualified controversies/trade-offs')
check(len(re.findall(r'^#### Q\d\d（',source,re.M))==10,'Ten questions with reasoning and design impact')
check(not re.search(r'\[[AD]\d+\]\[[AD]\d+\]', source), 'Adjacent citations cannot be misparsed as Markdown reference labels')
refs=source.split('## 8. References',1)[1]
used=set(re.findall(r'\[([AD]\d+)\]',source.split('## 8. References',1)[0]))
for ref in used:check(re.search(r'^\['+ref+r'\]: https://',refs,re.M) is not None,'Traceable reference '+ref)
check('results demonstrate' not in source.lower(),'No false completed-results phrase')
check(len(re.findall(r'^\| \[A[1-6]\]',source,re.M))==6,'Six AI article table rows')
check(len(re.findall(r'^\| \[D(?:1|3|6|7|8|9)\] [^|]+ \|',source.split('## 4.',1)[0],re.M))==6,'Six domain article table rows')
code=re.search(r'```text\n(.*?)\n```',design,re.S)[1].splitlines()
check([int(x.split()[0]) for x in code]==list(range(1,len(code)+1)),'Pseudocode has continuous 01–44 line numbering')
check(len(code)==44,'44-line canonical algorithm')
for name,block in zip(['architecture','flowchart'],re.findall(r'```mermaid\n(.*?)\n```',design,re.S)):
    check((ROOT/f'assets/refactor/{name}.mmd').read_text().strip()==block.strip(),'Diagram source matches DESIGN: '+name)
manifest=json.loads((ROOT/'assets/refactor/diagram-manifest.json').read_text())
for name,h in manifest.items():check(hashlib.sha256((ROOT/'assets/refactor'/name).read_bytes()).hexdigest()==h,'Rendered diagram hash: '+name)

base=ROOT/'openspec/changes/refactor-energy-proposal'
trace=(ROOT/'docs/refactor/traceability.md').read_text();tasktext=(base/'tasks.md').read_text()
requirements=[];scenarios=[]
for p in sorted((base/'specs').glob('*/spec.md')):
    t=p.read_text();requirements+=re.findall(r'^### Requirement: (ED-\w+)',t,re.M)
    scenarios+=re.findall(r'^#### Scenario: (.+)',t,re.M)
for req in requirements:check(req in trace,'Requirement traced: '+req)
for scenario in scenarios:check(scenario in trace,'Scenario traced: '+scenario)
check(len(requirements)==len(set(requirements))==14,'14 distinct proposed product requirements')
check(len(scenarios)==len(set(scenarios)),'Unique scenario IDs')
check(not re.search(r'^- \[x\] [234]\.\d',tasktext,re.M),'Future product tasks remain unchecked')
check(not (ROOT/'openspec/changes/archive/refactor-energy-proposal').exists(),'Unimplemented change is not archived')
check(len(list((ROOT/'openspec/specs').glob('*/spec.md')))==1,'Only existing document capability is in main specs')
check(not (ROOT/'src').exists(),'No placeholder product implementation claimed')

# Preserve every tracked original other than explicitly authorized documentation updates.
original=json.loads((ROOT/'docs/refactor/original-files.sha256.json').read_text())
allowed={'README.md','DESIGN.md','.gitignore'}
for name,h in original.items():
    if name not in allowed:check((ROOT/name).exists() and hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h,'Original preserved: '+name)

pptpath=ROOT/'deliverables/refactor/Proposal.pptx'
with zipfile.ZipFile(pptpath) as z:
    check(z.testzip() is None,'PPTX ZIP integrity')
    for entry in z.namelist():
        if entry.endswith(('.xml','.rels')):ET.fromstring(z.read(entry))
check(True,'All PPTX XML/relationships parse')
ppt=Presentation(pptpath);pdf=fitz.open(ROOT/'deliverables/refactor/Proposal-slides.pdf')
check(len(ppt.slides)==len(pdf)==len(json.loads((ROOT/'research/refactor/slides.json').read_text()))==27,'PPTX, PDF and page-source counts match (27; no Final threshold)')
ppttext='\n'.join(shape.text for slide in ppt.slides for shape in slide.shapes if shape.has_text_frame)
compact=lambda x:re.sub(r'\s','',x)
for line in code:check(compact(line) in compact(ppttext),'PPTX matches algorithm line '+line[:2])
for i,page in enumerate(pdf,1):
    check(bool(page.get_text().strip()),f'PDF page {i} contains text')
    for x0,y0,x1,y1,*_ in page.get_text('blocks'):
        check(x0>=-1 and y0>=-1 and x1<=961 and y1<=541,f'PDF page {i} text bounds')
check(all(slide.has_notes_slide for slide in ppt.slides),'All PPTX slides have source/notes')
pdf.close()

class Links(HTMLParser):
    def __init__(self):super().__init__();self.targets=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ('href','src'):self.targets.append(v)
paths=[ROOT/'README.md',ROOT/'DESIGN.md',ROOT/'research/proposal_refactored.md',*sorted((ROOT/'docs/refactor').glob('*.md')),base/'proposal.md',base/'design.md',ROOT/'deliverables/refactor/slides.md']
for p in paths:
    targets=re.findall(r'\]\(([^)]+)\)',p.read_text())
    for target in targets:
        if target.startswith(('http:','https:','#','mailto:')):continue
        check((p.parent/target.split('#')[0]).exists(),f'Local Markdown link resolves: {p.relative_to(ROOT)} -> {target}')
p=ROOT/'deliverables/refactor/Proposal.html';links=Links();links.feed(p.read_text())
for target in links.targets:
    if not target.startswith(('http:','https:','#','mailto:')):check((p.parent/target.split('#')[0]).exists(),'HTML local target resolves: '+target)
report={'scope':'Document/structure validation only; no Agent, energy or Office native rendering test','checks':len(checks),'requirements':len(requirements),'scenarios':len(scenarios),'slides':len(ppt.slides),'abstract_codepoints':count,'result':'PASS','details':checks}
(ROOT/'docs/refactor/document-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(f'PASS: {len(checks)} artifact checks; {len(requirements)} requirements; {len(scenarios)} scenarios; 27 slides; {count} abstract codepoints.')
print('Not validated: unimplemented product scenarios, real energy experiments, native Office rendering.')
