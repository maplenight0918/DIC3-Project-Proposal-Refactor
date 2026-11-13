# Energy Analysis

## Purpose

定義建築總表的可重算基準、校準門檻與候選事件輸出，限制訓練及測試資訊使用並避免把統計偏離誤稱節能或故障；此處描述未實作的預定數值能力，效能仍待實驗驗證。

## ADDED Requirements

### Requirement: ED-A01 時間隔離與固定基準

系統 SHALL 按預登錄8週train、2週calibration、2週test計算；B0只用train全域中位數，B1只用train星期小時中位數；各自門檻為calibration絕對殘差.99 linear分位數。查詢顯示範圍不得改變擬合。

#### Scenario: A01-no-leakage
- **WHEN** 只修改保留test觀測值或縮小報告顯示期間
- **THEN** B0/B1基準與校準門檻保持不變，兩方法共用相同有效測試點

#### Scenario: A01-zero-threshold
- **WHEN** 校準閾值為零且資料未提供可確認的電表解析度
- **THEN** 系統回INSUFFICIENT_DATA及不可校準原因，不任意指定小數替代

### Requirement: ED-A02 事件與量綱

系統 SHALL 以abs(residual)>threshold標記候選點，只合併相鄰同方向點；缺測、非警示與方向變化均中斷。只有確認固定區間電能才相加，輸出命名為相對基準偏離，禁止稱為已節電或已確診故障。

#### Scenario: A02-illustrative-event
- **WHEN** 說明fixture四個逐時有效值各180 kWh、基準各120、固定門檻30
- **THEN** 四點合為一事件且偏離240 kWh；標記illustrative_only，不作BDG2實測結果

#### Scenario: A02-missing-break
- **WHEN** 上述fixture第三小時缺測
- **THEN** 系統不補零、不跨缺口合併為四小時事件，分別計算兩段有效事件

#### Scenario: A02-equality-and-sign
- **WHEN** 殘差恰等於門檻或相鄰警示方向改變
- **THEN** 等於門檻者不標記，方向改變則另開事件

### Requirement: ED-A03 領域規則可撤回

系統 SHALL 僅評估具前提證據的領域規則，記錄rule_id、版本、支持／缺少證據及查核建議；工具失敗保留既有分析，不能把未執行規則寫成成立。

#### Scenario: A03-conditional-rule
- **WHEN** 有可靠作息、時間與偏高事件才選schedule_check
- **THEN** 系統列符合條件及待查排程假說，不直接宣告設備未關閉

#### Scenario: A03-rule-failure
- **WHEN** 合法規則工具在分析成功後失敗
- **THEN** 系統保存失敗，依既有數值產生DEGRADED報告，無該規則結果
