# Proposal

## Why

Energy Detective 已有研究提案及 DESIGN，但設計需求缺乏可驗收情境與任務追蹤，且原始提綱、簡報和工程文件容易漂移。本次將提案重構與未實作產品的設計規格化，使後續開發可依證據與驗收條件進行。

## What Changes

- 新增重構 Proposal、A–F與中英摘要、連貫緒論、分類文獻比較、5/3/10推理回答及評估規劃。
- 將 DESIGN 的未來產品行為轉為以下五項能力的 ADDED Requirements；均為擬議契約，並非已上線功能。
- 保留原提案與簡報，新增獨立可重建交付；建立需求、模組、scenario、任務及驗證追蹤。
- 主要 DESIGN 維護技術細節，這裡的 design.md 維護變更決策與引用，避免複製第二套架構。
- 本次只完成文件／規格任務；後續實作任務保持未勾選，change 不封存。

## Capabilities

### New Capabilities

- `query-control`: 範圍澄清、白名單、受限規劃、觀察後決策、預算與重試。
- `data-quality`: BDG2本機資料契約、歷史可見範圍、品質遮罩與條件式降級。
- `energy-analysis`: 時序隔離、B0/B1、校準、異常事件與可追查數值。
- `evidence-report`: 證據登錄、數值與語意邊界、模板降級、執行保存。
- `offline-evaluation`: 固定案例、對照／消融、分母與重現資訊。

### Modified Capabilities

無。既有程式只建置文件，另在主規格 `document-build` 描述其可觀察行為；沒有既有 Agent 行為可視為已完成規格。

## Impact

影響 README、DESIGN、新研究稿、文件產生與驗證腳本、新簡報及 OpenSpec/Codex整合。原有研究稿與交付檔保留；原有文件產生程式不變。安裝工具為 OpenSpec 2.0.0（Node >=22.12.0）；文件依賴沿用原requirements-docs。

非目標：本次不下載全BDG2、不呼叫LLM服務、不完成src、不聲稱通過產品情境、不做真實實驗、不做Final PPT／影片、不部署網站／建立遠端repo；後續已獲使用者授權推送DIC3文件至指定既有repository。數字為預登錄設計值而非已測性能。研究目標仍為原RQ1–RQ3。
