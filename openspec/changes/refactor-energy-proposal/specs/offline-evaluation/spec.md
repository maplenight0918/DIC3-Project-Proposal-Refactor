# Offline Evaluation

## Purpose

定義比較與驗證輸出的可重現要求、真值層級與分母，讓後續開發者能區分數值分析、生成文字與選工具各自的效果；所有結果尚待實作，本規格不會把文件檢查當成產品驗證。

## ADDED Requirements

### Requirement: ED-V01 公平比較與消融

評估器 SHALL 以相同資料及B1比較固定模板、固定流程加LLM、受限Agent；後兩者共用模型與報告提示詞，記錄差異與成本。另有離線證據驗證器消融及領域規則消融，禁止混入使用者輸出。

#### Scenario: V01-matched-comparison
- **WHEN** 執行C01–C10各三次及三組比較
- **THEN** 結果逐案例呈現任務成功、完整度、證據正確、未支持根因、規則次數、工具／LLM呼叫、tokens與時間，包含失敗

#### Scenario: V01-validator-ablation
- **WHEN** 對同一批錯誤草稿及正確控制啟用／停用驗證器
- **THEN** 分別報正確拒絕率及誤拒率；語意案例由人工審閱，不以ID檢查宣稱根因正確

### Requirement: ED-V02 真值與分母

評估器 MUST 區分原始無故障標籤、合成注入、人工審閱與現場真值；原測試集不變，注入副本用固定seed且不重訓。零分母記N/A，漏失事件延遲N/A並另報件數，不計真實故障precision/recall。

#### Scenario: V02-synthetic-events
- **WHEN** 用seed42在有效非重疊區間嘗試三類各10件注入
- **THEN** 保存實際件數、幅度、起訖與注入前已有警示，報各類命中／分母；不足不越界補足

#### Scenario: V02-empty-denominator
- **WHEN** 報告沒有數值fact或沒有可注入事件
- **THEN** 對應率記N/A而非100%，仍呈現必要資訊完整度及不足原因

### Requirement: ED-V03 可重現紀錄

評估器 SHALL 保存資料hash、程式版本、設定、seed、模型識別、提示詞版本、逐例紀錄及雙人審閱分歧；所有未執行指標保持待測，禁止用設計目標替代實測。

#### Scenario: V03-unimplemented
- **WHEN** 只有提案、規格和文件驗證而沒有產品實驗
- **THEN** MAE、命中、任務及追溯等欄位均標待測，不能把OpenSpec通過寫成Agent有效

#### Scenario: V03-reviewer-unavailable
- **WHEN** 只能取得一位審閱者或模型版本識別不完整
- **THEN** 保留實際資訊並揭露限制，不宣稱雙人一致或逐字可重現
