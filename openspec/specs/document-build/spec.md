# Document Build

## Purpose

記錄盤點時已存在且可驗證的文件建置行為：本專案能從Markdown與投影片資料產生提案文件及閱讀版本。這是已存在的文件工具能力，不代表Energy Detective的任何能源分析、Agent或實驗功能已實作。

## Requirements

### Requirement: DOC-B01 既有文件輸出

文件建置工具 SHALL 從既有研究稿及投影片資料產生DOCX、HTML、PPTX與PDF；輸出包含架構、流程與來源，且不需要能源資料或LLM API。

#### Scenario: B01-readable-artifacts
- **WHEN** 在既有文件依賴齊備下解析已產生的Proposal文件與簡報
- **THEN** DOCX/PPTX可由Office解析庫讀取，PPT與PDF頁數一致，文件含References及技術內容

### Requirement: DOC-B02 文件與產品狀態分離

文件 SHALL 明示系統處於Proposal階段，沒有可執行Agent、真實實驗或已實現節能結果。

#### Scenario: B02-proposal-status
- **WHEN** 閱讀既有README、DESIGN及提案結果說明
- **THEN** 使用者可辨識已交付文件與尚未實作系統的界線
