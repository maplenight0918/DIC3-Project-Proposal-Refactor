# Tasks

本次授權範圍為第1組文件／規格。第2–4組為後續產品開發，均未實作；不能因status顯示artifacts齊備而勾選或封存。依賴以任務ID表示。

## 1. 提案重構與設計規格化（本次）

- [x] 1.1 盤點原專案與七附件、Git狀態及來源分類；驗收docs/refactor/inventory.md與原檔hash。
- [x] 1.2 完成A–F、中文計數、英文摘要、G–L緒論與分類文獻；依賴1.1；驗收proposal_refactored與source-audit。
- [x] 1.3 補5/3/10推理與評估／消融協議；依賴1.2；驗收提案§4及evaluation.md，結果保持待測。
- [x] 1.4 CLI初始化、五能力spec與主要DESIGN關係；依賴1.1；驗收config、proposal/specs/design與追蹤矩陣。
- [x] 1.5 重建新簡報、HTML與圖表；依賴1.2–1.4；驗收產物可開啟及圖表/投影片實際呈現，不覆寫原檔。
- [x] 1.6 完成嚴格OpenSpec、文件一致與原檔保留檢查；依賴1.5；驗收validation.md、驗證JSON、README操作入口及A2Z/評分核對。

## 2. 資料與確定性分析（後續，未實作）

- [ ] 2.1 取得登錄BDG2單棟及metadata/weather、保存授權/commit/hash；依賴1.6；以D01-normalize/cutoff/unknown-unit fixture驗收，更新資料操作文件。
- [ ] 2.2 實作完整時間格點、品質遮罩、覆蓋與情境前提；依賴2.1；以D02三scenario與D03兩scenario測試，記錄原值/遮罩/分母。
- [ ] 2.3 實作B0/B1與固定時間校準；依賴2.2；以A01-no-leakage、zero-threshold驗收，修改test不改擬合或門檻，記錄設定版本。
- [ ] 2.4 實作事件合併及量綱證據；依賴2.3；用A02三scenario驗收240 kWh說明fixture、缺口、等號及方向，說明fixture不混入實測。

## 3. Agent、規則與報告（後續，未實作）

- [ ] 3.1 實作需求範圍及型別工具控制；依賴2.4；Q01三scenario與Q02-invalid-plan驗收，未知工具/路徑/越界不得執行，更新API契約。
- [ ] 3.2 串接一次觀察決策、呼叫預算與I/O重試；依賴3.1；Q02-adaptive-rules/no-event及Q03三scenario驗收，保存選擇與呼叫次數。
- [ ] 3.3 實作版本化領域規則與條件降級；依賴3.2；A03兩scenario及D03驗收，失敗仍保留既有分析，不確診設備。
- [ ] 3.4 實作Evidence/Claim比對及本地模板；依賴3.3；E01三scenario、E02-report-fallback/early-exit驗收，另人工審因果語意，記錄草稿/最終結果。
- [ ] 3.5 實作所有退出保存與寫檔失敗；依賴3.4；E02-save-error及K01–K12契約驗收，更新實際可執行README命令。

## 4. 離線評估與整合（後續，未實作）

- [ ] 4.1 實作原始/注入副本與成對指標；依賴2.4、3.5；以V02兩scenario及固定seed驗收，零分母N/A、漏失保留、實際件數可回查。
- [ ] 4.2 完成三組同資料比較與兩必要消融；依賴4.1；以V01兩scenario及協議成功判準驗收，連同成本/完整度報告，不預設Agent勝出。
- [ ] 4.3 兩人標註、重現紀錄與失敗分析；依賴4.2；V03兩scenario驗收，保存分歧與真值層級，未測欄位待測，缺人明示。

## Workflow follow-up

- 本次不archive或sync產品delta。全部產品任務與scenario有實際證據、完成審閱後才執行archive。
- Final PPT >20頁、影片 >10分鐘及正式實驗結論屬後續Final交付；本次依使用者後續授權提交DIC3文件至指定既有GitHub repository，不建立遠端repository。
