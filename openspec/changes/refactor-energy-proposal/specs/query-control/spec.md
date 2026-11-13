# Query Control

## Purpose

定義Energy Detective在取得明確建築與期間後，如何限制可執行工具、依分析觀察選擇後續調查，並在錯誤與預算耗盡時停止；這些是未實作的產品契約，不代表本次文件重構已完成執行功能。

## ADDED Requirements

### Requirement: ED-Q01 明確查詢範圍

系統 SHALL 要求building_id及半開區間[start,end)，驗證其位於登錄測試期內，禁止自行替換建築、日期或擴大範圍。

#### Scenario: Q01-valid-window
- **WHEN** 使用者提供清單內建築及測試期內有效期間
- **THEN** 系統接受查詢並在回應保留同一建築與期間

#### Scenario: Q01-missing-input
- **WHEN** 缺少建築或起訖時間
- **THEN** 系統回NEED_INPUT列出缺少欄位，不執行用電分析；使用者補充後另開一次執行

#### Scenario: Q01-out-of-range
- **WHEN** 查詢範圍超出登錄測試期或start不早於end
- **THEN** 系統列出可用範圍與錯誤，保留原問題，不自動改日期

### Requirement: ED-Q02 受限工具與觀察決策

系統 MUST 只執行白名單工具與型別化參數；品質、分析依賴不可跳過，分析後只允許一次選適用rule_ids或直接報告，保存選擇與跳過理由。資料文字不得改變固定設定。

#### Scenario: Q02-adaptive-rules
- **WHEN** 分析產生有效事件但缺天氣，Agent選歷史規則
- **THEN** 系統實際執行所選合法規則、不執行weather_context，並保存觀察與決策理由

#### Scenario: Q02-invalid-plan
- **WHEN** 計畫包含未知工具、任意程式、路徑、越界參數或要求更改門檻
- **THEN** 系統拒絕執行，至多依錯誤修正一次；仍不合法即FAILED並留紀錄

#### Scenario: Q02-no-event
- **WHEN** 品質合格且沒有候選事件，Agent選直接報告
- **THEN** 系統記錄跳過規則的理由，回傳無候選事件與資料限制，不創造異常

### Requirement: ED-Q03 有界呼叫與失敗

系統 SHALL 將所有實際工具呼叫含重試限制於10次，LLM限制於5次；只允許load_window暫時性I/O同參數重試一次。無證據可用時FAILED，有有效分析時可DEGRADED，本地模板及保存不需額外外部呼叫。

#### Scenario: Q03-transient-io
- **WHEN** 首次載入發生可重試的暫時I/O錯誤
- **THEN** 系統以相同參數重試一次並記錄兩次呼叫；再次失敗則停止

#### Scenario: Q03-permanent-failure
- **WHEN** 檔案不存在、欄位錯誤或解析／規劃LLM不可用
- **THEN** 系統不盲目重試，保存錯誤並停止，不虛構分析結果

#### Scenario: Q03-budget-exhausted
- **WHEN** 下一次呼叫會超過10次工具或5次LLM預算
- **THEN** 系統拒絕該呼叫，以現有證據產生受限輸出或FAILED，保存實際次數
