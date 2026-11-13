# DIC3 GitHub提交前核對

日期：2026-11-13。依使用者後續指示，檢查完成後提交至既有遠端 `https://github.com/maplenight0918/DIC3-Project-Proposal-Refactor.git`。工作位置為 `DIC3/Project_Proposal_Refactor/`，不修改Final_proj；初次查詢遠端沒有任何refs，因此使用main進行首次提交，不覆蓋遠端歷史。

## 要求核對

重新閱讀《期末專題提案作業規範.pdf》四頁。結論：本次「提案重構＋設計規格化」必要文件齊備；產品實作與正式實驗仍未完成，不能把規格驗證解讀為產品功能驗收。

| 本次要求 | 交付位置 | 狀態 |
|---|---|---|
| 安裝OpenSpec與spec-driven workflow | .openspec-version、openspec/config.yaml、[操作流程](workflow.md) | 2.0.0；CLI真實初始化，proposal/specs/design/tasks齊備 |
| A–F、中文摘要與英文版本 | [Proposal](../../research/proposal_refactored.md) §1 | 六段、299個非空白Unicode字元（含標點）、英文Title/Abstract/Index Terms |
| 5模式／3爭點／10深度問題 | Proposal §4 | 含證據、適用限制、立場代價、參考回答及設計／驗證影響 |
| DESIGN轉OpenSpec | [DESIGN](../../DESIGN.md)、[變更任務](../../openspec/changes/refactor-energy-proposal/tasks.md)、[追蹤矩陣](traceability.md) | 14項產品需求、36情境；本次6項完成，產品12項未完成，未封存 |
| Introduction重構 | Proposal §2 | 正式連貫文章與G–L、客觀動機、問題、缺口與預期貢獻 |
| Related Work重構 | Proposal §3、§8及[source-audit](source-audit.md) | AI與領域分類、12列8欄比較表、可追溯引用及研究缺口 |
| Agent＋領域＋分析＋應用 | Proposal §5與DESIGN | 八模組責任／介面／狀態、編號架構、分支流程、44行偽碼 |
| 評估規劃與誠實成果 | Proposal §6–7、[evaluation](../../research/refactor/evaluation.md) | baseline、ablation、ground truth、分母／切分／洩漏防範、失敗案例；實驗結果待測 |
| Proposal PPT | [新版PPTX](../../deliverables/refactor/Proposal.pptx)、[PDF](../../deliverables/refactor/Proposal-slides.pdf)、[逐頁稿](../../deliverables/refactor/slides.md) | 27頁，含動機、文獻、Gap、設計、架構、流程與偽碼，原29頁保留 |
| README／GitHub／完整度 | [README](../../README.md)、[驗收](validation.md)、[A2Z](a2z.md)、[修訂紀錄](revisions-and-next.md) | DIC3獨立根目錄與正確遠端、原始檔hash、建置／驗證／打包工具 |

依20／20／20／20／15／5比例的逐項檢查保留在validation.md；這是完整性檢查，不是預估教師給分。A2Z中的實驗與findings仍標為規劃，選配資訊圖不影響本次必要交付。

## 本次重跑與範圍

本次在DIC3作業目錄獨立建立Python環境，依requirements-docs.txt安裝，重建產物並執行新版及原版文件檢查。OpenSpec strict validation、doctor、status與apply任務狀態也在新根目錄重跑；最新JSON記錄新根目錄。命令、退出碼與結果保存在github-check.log，原commands.log保留第一輪證據。

檢查包括：中文摘要計數、5／3／10、引用入口、技術單一來源、原檔保留、14需求／36情境追蹤、44行偽碼與PPT一致、PPTX/XML、27頁PDF內容界限、Markdown/HTML本地連結，以及未實作任務未勾選。實際視覺檢查與原生Office限制詳見validation.md。

首次Git匯入的完整`diff --cached --check`指出原期中稿research/proposal_source.md末尾已有空白行；為保留原檔SHA-256不修改它。排除此原稿後，其餘提交檔案通過空白檢查，沒有衝突標記。

此次提交只納入專案來源、原版與新版交付、OpenSpec及驗收證據。課堂attachment、Python環境、原始能源資料、第三方研究全文與金鑰不納入。沒有建立遠端repo、force push、部署網站或封存產品變更。Git提交與遠端main的實際commit是提交是否成功的依據，文件中的planningComplete不是產品完成依據。

## 保留限制

沒有能源Agent實作、正式資料實驗或原生PowerPoint渲染測試。A5／A6只引已核實的預印本版本，正式出版狀態未獨立確認；D2未用於論證。資料建築／期間、LLM版本／成本及標註者留待產品開發確認。Final程式、>20頁Final PPT、>10分鐘影片與正式實驗結果不在本次範圍。
