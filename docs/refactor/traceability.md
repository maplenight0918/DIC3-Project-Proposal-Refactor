# 研究問題與需求追蹤

RQ1：B1與B0在相同有效測試點的基準品質。RQ2：選工具的額外價值、完整度與成本。RQ3：主張證據驗證與錯誤攔截。模組名稱及實作狀態以DESIGN為準，全部產品需求尚未實作。以下scenario為可驗收規劃；OpenSpec validate只檢查結構，不執行這些產品驗證。

| 研究問題 | 需求ID | 模組 | OpenSpec scenario（完整名稱） | 後續task | 驗證方式 |
|---|---|---|---|---|---|
| RQ1/RQ3 | [ED-D01](../../openspec/changes/refactor-energy-proposal/specs/data-quality/spec.md) | ③ | D01-normalize<br>D01-cutoff<br>D01-unknown-unit | 2.1 | 下載manifest、截止與單位fixture |
| RQ1 | [ED-D02](../../openspec/changes/refactor-energy-proposal/specs/data-quality/spec.md) | ④⑤ | D02-gap-versus-zero<br>D02-insufficient-coverage<br>D02-quality-tool-error | 2.2 | C06、K04；格點分母／缺口／衝突fixture |
| RQ2/RQ3 | [ED-D03](../../openspec/changes/refactor-energy-proposal/specs/data-quality/spec.md) | ④⑥ | D03-weather-missing<br>D03-timezone-unknown | 2.2/3.3 | C07、K11；天氣／作息獨立缺漏 |
| RQ1 | [ED-A01](../../openspec/changes/refactor-energy-proposal/specs/energy-analysis/spec.md) | ⑤ | A01-no-leakage<br>A01-zero-threshold | 2.3 | K05/K12；改test不改擬合與門檻 |
| RQ1 | [ED-A02](../../openspec/changes/refactor-energy-proposal/specs/energy-analysis/spec.md) | ⑤ | A02-illustrative-event<br>A02-missing-break<br>A02-equality-and-sign | 2.4 | 240 kWh說明例、缺口、等號、方向fixture |
| RQ2/RQ3 | [ED-A03](../../openspec/changes/refactor-energy-proposal/specs/energy-analysis/spec.md) | ⑥ | A03-conditional-rule<br>A03-rule-failure | 3.3 | K06；規則前提與失敗保留證據 |
| RQ3 | [ED-E01](../../openspec/changes/refactor-energy-proposal/specs/evidence-report/spec.md) | ⑦ | E01-valid-claim<br>E01-mismatched-claim<br>E01-unsupported-cause | 3.4 | C10、K08；四類置錯＋正確控制＋人工語意 |
| RQ2/RQ3 | [ED-E02](../../openspec/changes/refactor-energy-proposal/specs/evidence-report/spec.md) | ⑦ | E02-report-fallback<br>E02-early-exit<br>E02-save-error | 3.4/3.5 | K07/K09；LLM失敗模板、提前退出與寫檔失敗 |
| RQ2/RQ3 | [ED-V01](../../openspec/changes/refactor-energy-proposal/specs/offline-evaluation/spec.md) | ⑧ | V01-matched-comparison<br>V01-validator-ablation | 4.2 | 三組逐例公平比較、驗證器／規則消融 |
| RQ1 | [ED-V02](../../openspec/changes/refactor-energy-proposal/specs/offline-evaluation/spec.md) | ⑧ | V02-synthetic-events<br>V02-empty-denominator | 4.1 | seed42注入副本、零分母、實際件數 |
| RQ1/RQ2/RQ3 | [ED-V03](../../openspec/changes/refactor-energy-proposal/specs/offline-evaluation/spec.md) | ⑧ | V03-unimplemented<br>V03-reviewer-unavailable | 4.3 | 版本manifest及雙人分歧／缺人限制 |
| RQ2 | [ED-Q01](../../openspec/changes/refactor-energy-proposal/specs/query-control/spec.md) | ① | Q01-valid-window<br>Q01-missing-input<br>Q01-out-of-range | 3.1 | C04/C05；合法與越界期間fixture |
| RQ2 | [ED-Q02](../../openspec/changes/refactor-energy-proposal/specs/query-control/spec.md) | ②⑥ | Q02-adaptive-rules<br>Q02-invalid-plan<br>Q02-no-event | 3.1/3.2 | C03/C07/C09；檢查實際呼叫與跳過理由 |
| RQ2/RQ3 | [ED-Q03](../../openspec/changes/refactor-energy-proposal/specs/query-control/spec.md) | ②⑦ | Q03-transient-io<br>Q03-permanent-failure<br>Q03-budget-exhausted | 3.2/3.5 | C08、K01/K02/K03/K10；計數及錯誤注入 |

既有行為對照：DOC-B01/DOC-B02 → 文件建置程式／README → B01-readable-artifacts/B02-proposal-status → 本次1.1/1.6 → 既有verify_deliverables.py解析原輸出。此行不歸入產品RQ，不混淆文件與研究驗證。

本次文件任務1.2/1.3交付提案與評估；1.4交付DESIGN/specs；1.5/1.6交付簡報與驗證。每項後續task具依賴與驗收方式，見tasks.md。
