# 盤點與作業需求對照

盤點日期：2026-11-13。開始時 Git `status --short` 為空，HEAD `ab6b492`（Label proposal documents and presentation as Group 25）。`/Final_proj` 不存在；依使用者補充在上一層找到 `../Final_proj/energy-detective-agent`，為當時盤點的原專題 Git repository；當時工作區 DIC3 本身不是 Git repository。現在本次作業位於 `DIC3/Project_Proposal_Refactor/`，使用獨立DIC3 repository，原始盤點紀錄與hash保留。根目錄至專案下未發現適用的 AGENTS.md；其他專案的 AGENTS.md 不適用。

## 來源辨識與閱讀紀錄

| 實際來源 | 內容確認 | 用途 |
|---|---|---|
| `research/proposal_source.md`、`deliverables/Proposal.docx` | Energy Detective，第25組，總表異常調查、BDG2、受限工具及證據報告 | 本專題原始提案；保留 |
| `deliverables/Proposal.pptx`、`Proposal-slides.pdf` | 29頁 Energy Detective；含八模組、流程、偽碼、三研究問題；PPTX 無獨立備註頁 | 本專題原始簡報；保留 |
| `README.md`、`DESIGN.md`、`research/*.md` | 單棟歷史重播；B0/B1；未實作；無實驗結果 | 主題與工程進度依據 |
| `scripts/*.py`、`requirements-docs.txt` | 文件合成、Office/HTML/PDF產生及文件驗證 | 已存在的文件工具，不是 Agent 程式 |
| `../*.rar` | 既有提案壓縮檔；已有可閱讀的解壓專案 | 保留，未另解壓覆寫 |
| `../../DIC3/attachment/期末專題提案作業規範.pdf`（實際附件目錄見下） | 4頁；Proposal/Final分流、20/20/20/20/15/5評分 | 必要內容與交付依據 |
| `A2Z outline example.pdf` | 1頁，2020 A-Z SOP；G–L緒論，PA–PM方案，Q–V實驗 | 文章組織；定義依原PDF，不依資訊圖改寫 |
| `期中Proposal_熱量AI_Agent.docx` | Nutrition/DietSense；食物資料、TDEE、500筆及20人7天均為該範例內容 | 教學範例，不移植其主題、指標或文獻 |
| `DietSense_Proposal_Presentation.pptx` | 22頁及22個備註XML；備註只有頁碼；第13頁區分估計區間與信賴區間，第21頁提醒暫定引用 | 看過投影片文字、結構及備註；不直接改標題當成果 |
| `1.NBLM output 熱量AI提案解析.pdf`、`熱量AI提案解析.pdf` | 各4頁，逐頁擷取文字完全一致，二進位 SHA-256 不同 | 重複解析，非獨立證據 |
| `2.DietSense資訊圖表.png` | 已實際開圖；高密度總結，含未核實範例數字；A2Z右欄部分定義與原PDF不同 | 僅呈現方式參考，不作研究證據或A2Z定義來源 |
| 教師 GitHub README、myplan/2026-11-11-DietSense-conversation-plan.md | DietSense構想與課堂對話紀錄；含空品表述練習且明示不是DietSense規格 | 教學參考；不是本專題實作模板 |

附件實際絕對目錄：`/user_data/IoT/DIC3/attachment`；從目前DIC3作業根目錄相對路徑為 `../attachment`（原專題時為 `../../DIC3/attachment`）。全部七檔已開啟並擷取內文或看圖；PDF頁面、Word表格、PPT文字與備註均納入辨識。原始檔雜湊見 `attachments.sha256.json`。教師來源：<https://github.com/huanchen1107/2026-11-11-DIC3-ProjectRefactor>（GitHub網頁讀取失敗後以官方GitHub API及raw成功讀取）。

## 事實、計畫、假設與缺口

| 類型 | 判定 | 證據／處理 |
|---|---|---|
| 事實：已完成 | 提案、設計、29頁PPT、文件建置與驗證程式 | Git已追蹤檔；可檢查XML及既有文件驗證 |
| 事實：部分完成 | 原緒論有內容但以A–F提綱組織；5/3/10有題目及判讀要點；實驗協議有分母 | 改為連貫G–L論證、補口試推理回答及明確成功判準 |
| 事實：尚未實作 | 沒有src/、應用requirements.txt、config/experiment.json、資料集、產品測試或實驗輸出 | 不建立假產品；未來任務保持未勾選 |
| 事實：OpenSpec | 開始時無CLI、無openspec/；Node 22.20.0、npm 10.9.3 | 安裝及初始化詳見validation與workflow文件 |
| 規劃 | 校園／辦公設施管理、單棟BDG2、八模組、三組比較 | 所有產品能力均標規劃 |
| 合理假設 | 繁中CLI足以展示；12週8/2/2切分、90%覆蓋、10次工具預算 | 沿用原設計，理由與調整程序寫入提案；不是領域標準 |
| 待確認 | 真實building ID、日期、授權快照、LLM版本、兩位審閱者、課程截止日與分工 | 不阻擋本次文件；列於後續清單 |
| 證據不足 | 管理者需求尚無訪談，Agent增益與省時未測，無設備根因／節電真值 | 降為情境與待驗證假設，不作findings |

## 作業要求 → 原始位置 → 缺口 → 修訂 → 交付

| 作業要求 | 原始內容位置 | 缺口 | 修訂內容 | 交付檔案（相對專案根） |
|---|---|---|---|---|
| 安裝OpenSpec與SDD | 無 | 無CLI與規格生命週期 | 真實init、固定版本、現況與提案分流 | `openspec/`、`docs/refactor/workflow.md` |
| A–F＋中英摘要 | proposal_source §1 | 無可重算300字與英文版本 | 六段、中文計數、英文Title/Abstract/Index Terms | `research/proposal_refactored.md` §1 |
| 5/3/10 | domain_research | 適用邊界及推理回答不足 | 五模式、三取捨、十問推理與設計影響 | 同上 §4 |
| DESIGN轉OpenSpec | DESIGN.md | 無可驗收scenario、任務依賴與ID | 五個未來能力規格、既有文件建置規格、追蹤矩陣 | `DESIGN.md`、`openspec/`、`docs/refactor/traceability.md` |
| Introduction 20% | domain_research的A–F標題 | 正文較像提綱 | G–L連貫文章、明確貢獻層次 | 重構提案 §2 |
| Related Work 20% | ai_research＋domain_research | 需本次回查、2026近似研究 | 分類比較、AI／領域表、收斂研究缺口 | 重構提案 §3、`docs/refactor/source-audit.md` |
| Deep Research 20% | domain_research | 爭論排名無證據 | 明示爭點是工程／方法取捨，不宣稱全領域前三 | 重構提案 §4 |
| Agent與架構20% | proposed_scheme、DESIGN | 多副本漂移風險 | DESIGN為技術唯一編輯源；編號八模組及契約 | 重構提案 §5、`assets/refactor/` |
| 流程／偽碼／可行性15% | DESIGN Algorithm | 分支與圖輸出需一致 | 流程例外補齊、行號及工具預算定義 | 同上、重構簡報 |
| GitHub／DESIGN／完整度5% | 既有Git repo、README | 無本次提交入口 | 文件入口、可重建流程、檢查紀錄；依後續授權提交DIC3遠端 | `README.md`、`docs/refactor/validation.md` |
| Proposal PPT | deliverables/Proposal.pptx | 未含重構與OpenSpec | 保留原檔，新版簡報及逐頁稿 | `deliverables/refactor/Proposal.pptx`、PDF、slides.md |
| A2Z檢查 | 課堂原PDF | 無本專題對應 | 保留原定義；U/V/Y列待測，PM不偽造證明 | `docs/refactor/a2z.md` |
| 後續Final | docs/acceptance.md | 產品尚未完成 | 程式、實驗、>20頁Final與>10分鐘影片另列 | `docs/refactor/revisions-and-next.md` |
