# Design

## Context

變更動機見[proposal](proposal.md)。本專案現有程式僅建置文件；主規格document-build記錄既有行為，五份delta規格描述未來產品。使用spec-driven schema；所有產品任務尚未執行，change維持active。

## Goals / Non-Goals

技術細節以[主要DESIGN](../../../DESIGN.md)為唯一編輯來源，含Architecture、Components、Data Flow、AI Model、Domain Knowledge、Algorithm、Implementation Mapping、Results與Limitations。評估唯一來源為[評估協議](../../../research/refactor/evaluation.md)。本文件只維護跨文件決策，不再複製八模組或偽碼。生成的Proposal技術章節以標記區塊從兩來源更新。

目標是可重算、可追查、可停止的總表調查契約；非目標為任意程式執行、設備控制、現場故障確診及本次產品實作。

## Decisions

| 決策 | 採用與理由 | 替代方案與代價 |
|---|---|---|
| ADR01 文件與產品狀態分流 | main specs只放已有文件能力；change保存產品設計 | 把設計直接當已完成spec會誤導接手者；不提前sync/archive |
| ADR02 技術唯一編輯來源 | DESIGN負責架構/介面；evaluation負責分母；OpenSpec負責需求scenario | 全文複製多份易漂移；生成區塊與驗證器需維護 |
| ADR03 固定工具與一次觀察決策 | 白名單、型別、依賴、工具10次與LLM5次 | 自由程式生成更靈活但難驗收；固定全部流程較便宜，是RQ2對照 |
| ADR04 raw＋品質遮罩 | 保留可疑讀值，與缺測分離；同場址天氣 | cleaned可能刪除目標事件；保留raw增加不確定事件 |
| ADR05 簡單B0/B1 | 分離可重現分析與Agent效益；按時間隔離 | 天氣／基礎模型可改善表達能力但增加範圍與歸因混淆 |
| ADR06 主張契約與模板 | 對象、期間、單位、值、ID共同驗證 | 只檢ID不足；全面語意自動驗證不在最低可保證範圍，仍人工核對 |
| ADR07 本地失敗閉合 | 無核心資料停止；有分析時情境／報告降級；保存所有退出 | 無限制重試成本不可控；模板表達彈性較低 |

各ADR之可觀察行為見五個spec；研究問題→需求→模組→scenario→任務→驗證見[追蹤矩陣](../../../docs/refactor/traceability.md)。完整I/O以DESIGN「工具輸入與輸出」「預定資料契約」「模組責任與交換契約」為準。

## Risks / Trade-offs

- 單棟與品質選樣 → 限制外推，跨場址留後續；不假裝代表臺灣校園。
- 時區及量測解析度不完整 → 停相依規則或不可校準，不猜數字。
- LLM語意與版本不穩 → 記錄版本、固定提示、三次重跑、雙人審閱；不保證逐字重現。
- 文件通過不等於產品通過 → 任務分文檔1.x及產品2.x–4.x，產品fixture留待實作。
- A6已有高度近似系統 → 不宣稱Agent/工具選擇首創；以總表限制與公平比較驗證情境價值。

## Migration Plan

本次新增重構目錄，原始交付與研究稿保留；README指向新入口。重建僅寫deliverables/refactor及assets/refactor，主要設計與原始檔hash可比對。需撤回本版時可改README入口回原交付，不刪檔、不重置Git。產品未部署，沒有資料庫遷移或遠端發布。

日後依tasks順序實作；每一scenario有測試證據才勾該產品任務。全部完成並人工確認後才考慮archive（會同步main specs）；目前不得封存。

## Open Questions

真正building ID／12週期間待依品質規則選定；LLM供應商及精確版本待可用帳號決定；兩位審閱者與課程截止日待組員安排。這些可延後填入固定契約，不影響本次可審核設計；若資料不符須先更新協議再測試。
