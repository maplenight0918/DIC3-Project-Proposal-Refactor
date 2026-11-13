# DIC3 — Project Proposal Refactor using OpenSpec

專題：Energy Detective：建築用電異常調查 AI Agent

作業性質：個人作業

「物聯網數據分析與應用」DIC3個人作業：以既有專題提案進行重構與OpenSpec設計規格化。本階段交付研究、系統設計與簡報，系統程式與實驗尚未完成。

DIC3作業 Repository：<https://github.com/maplenight0918/DIC3-Project-Proposal-Refactor>。

本repository為DIC3個人作業，從既有Energy Detective期中專題重構而來；原始提案與簡報保留於research/與deliverables/。本地後續工作位置為`DIC3/Project_Proposal_Refactor/`，不再以Final_proj作為本次作業工作目錄。

## DIC3重構版：現在的閱讀與提交入口（2026-11-13）

本次完成提案重構與設計規格化；沒有實作能源Agent或執行能源實驗。原始Proposal與簡報保留，以下是新增版本。

- [完整重構Proposal](research/proposal_refactored.md)：A–F、299字中文摘要、英文Title/Abstract/Index Terms、Introduction、Related Work、5/3/10、技術與評估。
- [瀏覽器閱讀版](deliverables/refactor/Proposal.html)：下載整個專案後開啟，圖表與本地連結使用相對路徑。
- [新版Proposal PPTX](deliverables/refactor/Proposal.pptx)、[27頁簡報PDF](deliverables/refactor/Proposal-slides.pdf)、[完整逐頁稿](deliverables/refactor/slides.md)。這是Proposal，不抵充Final實驗簡報。
- [主要設計](DESIGN.md)與[現行評估協議](research/refactor/evaluation.md)：技術與評估的唯一編輯來源。
- [OpenSpec變更提案](openspec/changes/refactor-energy-proposal/proposal.md)、[規格](openspec/changes/refactor-energy-proposal/specs/)、[設計決策](openspec/changes/refactor-energy-proposal/design.md)、[任務](openspec/changes/refactor-energy-proposal/tasks.md)。產品任務未勾選、未封存。
- [盤點／需求與交付對照](docs/refactor/inventory.md)、[研究需求追蹤](docs/refactor/traceability.md)、[A2Z原定義對應](docs/refactor/a2z.md)。
- [原始來源查核](docs/refactor/source-audit.md)、[修訂與待補清單](docs/refactor/revisions-and-next.md)、[最終驗收紀錄](docs/refactor/validation.md)、[OpenSpec操作](docs/refactor/workflow.md)。

### 重建與驗證重構版

在本Git根目錄執行。Python文件套件沿用原requirements-docs；已有`.build-deps`可直接執行後兩行。

```bash
python3 -m venv .build-deps
.build-deps/bin/python -m pip install -r requirements-docs.txt
.build-deps/bin/python scripts/build_refactor.py
.build-deps/bin/python scripts/verify_refactor.py
```

Windows可將`.build-deps/bin/python`換為`.build-deps\Scripts\python.exe`。一般重建使用已提交PNG與雜湊，無需網路或Mermaid。修改DESIGN中的圖後必須重新渲染；程式會拒絕使用過期圖。

```bash
# 僅第一次準備圖表工具；Node >=22.12
npm install --prefix .build-diagrams @mermaid-js/mermaid-cli@11.12.0
MMDC="$PWD/.build-diagrams/node_modules/.bin/mmdc" .build-deps/bin/python scripts/build_refactor.py --render-diagrams
```

Mermaid需要可用Chromium與中文字型；可設`CHROME_BIN`指向瀏覽器，使用Droid Sans Fallback或替代CJK字型。預設無系統字型時請安裝CJK字型再重建圖。圖表來源位於assets/refactor，完整架構／流程由DESIGN更新；三張投影片流程為同流程的分段摘要。

```bash
npm install --global @fission-ai/openspec@2.0.0  # 已有2.0.0可跳過
export OPENSPEC_TELEMETRY=0
openspec status --change refactor-energy-proposal --json
openspec validate --all --strict --no-interactive --json
```

OpenSpec已用CLI初始化，不需重跑init。文件編輯完成後建置＋驗證；實作產品時依tasks依賴逐項驗收再勾選。當前不要archive或sync尚未實作的產品需求。CLI嚴格驗證通過只代表規格結構，不代表產品通過情境。

### 提交方式

本repository包含本次DIC3可重建來源與交付。使用者已授權提交並推送至上述DIC3遠端；[提交前核對](docs/refactor/github-submission-check.md)記錄範圍、驗證與限制。可提交此GitHub網址，或使用Code → Download ZIP下載完整檔案。若老師只收檔案，交重構Proposal Markdown、27頁PPTX（可附PDF）、DESIGN與完整openspec/及docs/refactor/；圖表請連同assets/refactor/提供。`deliverables/refactor/submission.zip`是同一批來源與產物的可攜副本，生成方式見validation。

`build_refactor.py`只更新新交付、圖表及Proposal的DESIGN/EVALUATION標記區塊；其餘論述直接編輯重構稿，一般簡報文字編輯research/refactor/slides.json，偽碼從DESIGN自動更新。下方是保留的期中版本說明，舊build_all.py只用於重建期中歷史交付，不用來產生本次新版。

## 提案交付（期中原版，保留）

- [Proposal.docx](deliverables/Proposal.docx)：提案文件（可編輯）。
- [Proposal.html](deliverables/Proposal.html)：下載後可在瀏覽器閱讀與列印的提案文件；請連同 `assets/` 圖檔下載。
- [Proposal.pptx](deliverables/Proposal.pptx)：Proposal 簡報（可編輯）。
- [Proposal-slides.pdf](deliverables/Proposal-slides.pdf)：簡報閱讀版。
- [DESIGN.md](DESIGN.md)：架構、元件、資料流、演算法、實作對應與預定驗證方式。
- [research/](research/)：查核來源與整合前研究稿。
- [完整提案 Markdown](research/proposal_source.md)：可直接在 GitHub 閱讀。
- [實驗協議](research/evaluation_protocol.md)：研究問題、選樣、十個案例、指標、三組對照與結果表。
- [作業與交付核對](docs/acceptance.md)：Proposal 評分對照及 Final Handover 待完成事項。

期中原版修訂補入建築模型適應的 2025 研究，形成 5 篇 AI＋5 份領域來源；十個深度問題另附判讀要點。Proposal PPT 為 29 頁，仍是提案簡報，不能代替包含實測結果的 Final PPT。

## 專題介紹

以 Building Data Genome 2 公開歷史建築電表及天氣資料，設計能選用分析工具、檢查資料品質、辨識異常用電時段並提供附帶證據調查建議的領域 Agent。透過歷史資料重播示範 IoT 資料分析流程；不需要購買感測器。

Agent 的輸出是待查假說與下一步檢查建議，不能僅憑總表證明設備故障，也不能把異常用電估計當成已驗證的節能量。

## 資料來源

- Building Data Genome 2：<https://github.com/buds-lab/building-data-genome-project-2>
- 資料論文：<https://doi.org/10.1038/s41597-020-00712-x>
- 下載與再散布前應遵守原資料庫授權、保留來源及必要聲明。本 Repository 目前不包含原始資料。

## Installation / How to Run / Demo

Proposal 文件可直接開啟，不需要安裝應用程式。系統尚在設計階段，目前沒有可執行的 Agent 或 Demo；預定環境、入口及資料準備步驟詳見 `DESIGN.md`，其中標為規劃中的指令尚不能執行。

正式實作時須補上鎖定版本的依賴、資料下載與前處理、啟動指令、測試方式及 Demo。不得把規劃指令視為已通過驗證。

## 重建 Proposal 文件（現在可執行）

需要 Python 3.9 或以上。從專案根目錄執行，依作業系統選一組；這些指令只重建文件，不會呼叫 LLM API 或執行用電實驗。

Linux／macOS：

```bash
python3 -m venv .build-deps
.build-deps/bin/python -m pip install -r requirements-docs.txt
.build-deps/bin/python scripts/build_all.py
```

Windows PowerShell：

```powershell
py -m venv .build-deps
.build-deps\Scripts\python.exe -m pip install -r requirements-docs.txt
.build-deps\Scripts\python.exe scripts/build_all.py
```

產物為 `deliverables/Proposal.docx`、`Proposal.html`、`Proposal.pptx`、`Proposal-slides.pdf` 及兩張 `assets/` 圖。預覽 PDF 使用 PyMuPDF 內建中文字型，不再依賴 Windows 路徑；可透過 `ENERGY_DOC_FONT` 指定本機字型檔。PPTX 使用可編輯文字與圖形，Office 顯示結果可能受字型替代影響，繳交前仍須開啟檢查。

文件來源與建置順序：

1. 編輯 `research/domain_research.md`、`ai_research.md`、`proposed_scheme.md` 與 `evaluation_protocol.md`。
2. `assemble_proposal.py` 合成 `research/proposal_source.md` 及簡報前半部；摘要與前半部簡報內容在該腳本中。
3. `finish_slides.py` 加入技術、驗證與交付簡報；`build_deliverables.py` 產生各格式。
4. `verify_deliverables.py` 驗證 Office XML、頁數一致、PDF 邊界、文獻／問題數量、偽碼行號與本機連結。

`proposal_source.md`、`slides_base.json`、`slides.json` 與交付檔是產生檔，直接修改後會在重建時被覆寫。若修改系統方法，也須同步更新 `DESIGN.md`；請以實驗協議作為案例與指標定義的共同依據。

常見問題：找不到 `fitz` 或 `markdown` 時，確認使用上面虛擬環境的 Python；產生程式若報文字溢出，拆頁或縮短文字後重新建置；HTML 圖片無法顯示時，確認保留 `assets/` 與 `deliverables/` 的相對位置。

## 研究問題與成功條件

- RQ1：B1 是否比 B0 更符合保留期間的用電型態？以同一批有效點比較 MAE。
- RQ2：Agent 能否維持必要資訊與證據品質，同時減少不必要規則評估？比較固定模板、固定流程＋LLM、受限 Agent。
- RQ3：證據檢查能否拒絕錯 ID、數值、單位與對象？以故意置錯的契約案例和人工語意審閱驗證。

失敗與零改善也是結果。所有效能欄位目前是「待測」；[合成計算例](research/proposed_scheme.md)僅用來解釋 240 kWh 偏離量的算法，不是 BDG2 的實驗成果。

## 階段狀態

本 Repository 收錄 Proposal 文件、PPT 與 DESIGN.md。期末實作須另完成真實實驗、結果比較、結論、至少 21 頁 Final PPT，以及超過 10 分鐘的 YouTube 簡報與 Demo。
