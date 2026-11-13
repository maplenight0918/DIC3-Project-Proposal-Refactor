# Data Quality

## Purpose

定義公開歷史建築電力資料的可追查輸入、時間可見範圍與品質分流，使使用者可以區別有效量測、缺值和不足證據；資料與程式尚未建置，所有條件是後續產品的驗收契約。

## ADDED Requirements

### Requirement: ED-D01 資料來源與重播邊界

系統 SHALL 僅讀登錄BDG2 raw electricity與對應metadata/weather，保存版本、SHA-256、授權來源及原始列欄定位；正規化電表身分、單位及時間語意，且不得暴露replay_until之後的觀測。

#### Scenario: D01-normalize
- **WHEN** 登錄檔案存在且欄位可辨識
- **THEN** 系統輸出單棟電力長表、場址天氣關聯、資料版本與來源定位，不混入非電力表

#### Scenario: D01-cutoff
- **WHEN** 檔案含replay_until之後的觀測
- **THEN** 後續工具與LLM都無法讀取超過截止timestamp的資料

#### Scenario: D01-unknown-unit
- **WHEN** 單位、區間標記語意或時間索引無法確認
- **THEN** 系統回INSUFFICIENT_DATA，不計算異常能量總和

### Requirement: ED-D02 品質遮罩與覆蓋

系統 SHALL 以完整時間格點為分母檢查各段至少90%有效，訓練星期小時組至少4個有效值；不補零或插補測試用電。相同重複可去重留紀錄，衝突／非有限／未解釋負值遮罩，缺測中斷事件。

#### Scenario: D02-gap-versus-zero
- **WHEN** 輸入同時存在有效零值、缺值及衝突重複
- **THEN** 系統保留有效零值、遮罩缺值與衝突，不將其補成零，覆蓋分母仍為完整時間格點

#### Scenario: D02-insufficient-coverage
- **WHEN** 任一分段有效率不足90%或任一訓練星期小時組不足4點
- **THEN** 系統輸出INSUFFICIENT_DATA與具分母的品質證據，不擬合B1

#### Scenario: D02-quality-tool-error
- **WHEN** 品質工具執行出錯而無法產生可靠遮罩
- **THEN** 系統回FAILED並保存錯誤，不跳過品質直接分析

### Requirement: ED-D03 情境資料降級

系統 SHALL 在天氣無法對齊時停weather_context；無可靠作息與當地時間時停schedule_check，仍允許品質合格的歷史用電分析並明示限制。

#### Scenario: D03-weather-missing
- **WHEN** 電力資料合格但同場址同時間天氣缺漏
- **THEN** 系統保留用電分析，以DEGRADED明示缺天氣且不產生氣溫解釋

#### Scenario: D03-timezone-unknown
- **WHEN** 原時間索引可比較但無可靠時區或使用者作息
- **THEN** 系統不猜UTC或週末停工，停用作息規則並保存理由
