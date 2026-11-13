# Evidence Report

## Purpose

定義報告中每個數值與事實如何連回資料、工具與適用範圍，以及引用失敗、生成失敗與保存失敗時的可觀察輸出，避免把文句流暢當成真實證據；本能力仍為待實作產品規格。

## ADDED Requirements

### Requirement: ED-E01 主張層級追溯

系統 MUST 對每個數值fact比對唯讀Evidence中的ID、field、建築、期間、單位與原值；顯示僅允許預登錄精度四捨五入。報告分離觀察、假說、缺少證據與下一步，不能以正確ID支持無根據根因。

#### Scenario: E01-valid-claim
- **WHEN** 工具證據與主張所有對象、期間、單位及值均相符
- **THEN** 報告保留可定位的證據ID與限制，審閱者能回查原始列欄

#### Scenario: E01-mismatched-claim
- **WHEN** 草稿含不存在ID、錯值、錯單位或同值但不同建築／期間
- **THEN** 系統拒絕該草稿，最終報告改從已驗證證據產生，不把錯誤內容當事實發布

#### Scenario: E01-unsupported-cause
- **WHEN** 使用者要求從總表證據確診特定空調故障或已節電量
- **THEN** 報告說明證據不足，僅給可查核的假說及所需設備／介入紀錄

### Requirement: ED-E02 確定性降級與保存

系統 SHALL 在報告工具失敗或驗證不通過時採本地固定模板；每條終止路徑保存request、狀態、既有證據、警告與呼叫紀錄。無分析不得假裝已完成；寫檔失敗須非零退出並明示未保存。

#### Scenario: E02-report-fallback
- **WHEN** 已有有效分析但報告LLM不可用或草稿驗證失敗
- **THEN** 系統不再重試LLM，以本地模板輸出DEGRADED並記錄降級原因及原草稿（若有）

#### Scenario: E02-early-exit
- **WHEN** 需求不足、核心資料不足或工具失敗導致提前停止
- **THEN** 系統保存對應NEED_INPUT、INSUFFICIENT_DATA或FAILED及已取得證據，不計為一般成功

#### Scenario: E02-save-error
- **WHEN** 無法寫出執行結果
- **THEN** 系統向stderr明示PERSISTENCE_ERROR並非零退出，不顯示已保存
