# OpenSpec 2.0.0：本專案工作流程

在Git根目錄 `energy-detective-agent` 操作。已檢查原環境沒有OpenSpec；Node v22.20.0、npm 10.9.3符合官方Node >=22.12.0需求，安裝npm registry回傳的2.0.0並固定在 `.openspec-version`。本次實際安裝是global CLI；不引入應用package.json或假Agent入口。

官方來源：[安裝與概觀](https://github.com/Fission-AI/OpenSpec)、[目前CLI](https://openspec.dev/docs/cli)、[v2.0.0 CLI文件](https://github.com/Fission-AI/OpenSpec/blob/v2.0.0/docs/cli.md)。官方舊文件有opsx示例；以已安裝CLI help及init產生的 `.agents/skills/` 為準。

## 已執行初始化

```bash
node --version
npm --version
npm view @fission-ai/openspec version engines --json
npm install --global @fission-ai/openspec@2.0.0
openspec --version
OPENSPEC_TELEMETRY=0 openspec init --tools codex --language '繁體中文' --no-animation
OPENSPEC_TELEMETRY=0 openspec new change refactor-energy-proposal
openspec instructions proposal --change refactor-energy-proposal --json
openspec instructions specs --change refactor-energy-proposal --json
openspec instructions design --change refactor-energy-proposal --json
openspec instructions tasks --change refactor-energy-proposal --json
```

初始化真實產生config與六個Codex skills；不是手建空資料夾。接續依schema寫proposal→specs/design→tasks；本次不呼叫產品apply，不封存。電腦已有相容2.0.0時直接使用，不必升級。

## 現在可執行的檢查

```bash
export OPENSPEC_TELEMETRY=0
openspec list --specs
openspec list
openspec show refactor-energy-proposal --type change
openspec status --change refactor-energy-proposal --json
openspec instructions apply --change refactor-energy-proposal --json
openspec validate --all --strict --no-interactive --json
.build-deps/bin/python scripts/verify_refactor.py
```

`instructions apply`只讀任務指引，不執行產品。`status`的planningComplete或artifact done表示檔案齊備；請同時看tasks完成數，不能當成產品完成。完整驗證記錄見validation.md。

## 文件與規格角色

| 檔案 | 責任 |
|---|---|
| research/proposal_refactored.md | 論證與研究文字；DESIGN/EVALUATION標記區塊由建置同步，不手改 |
| DESIGN.md | 現行技術設計的唯一編輯源；八模組、介面、圖、偽碼、狀態 |
| research/refactor/evaluation.md | 現行評估設計的唯一編輯源；參數、分母、判準、案例 |
| openspec/specs/document-build | 已有文件建置行為；沒有Agent已實作主張 |
| openspec/changes/refactor-energy-proposal/specs | 擬議產品的可驗收需求，尚未同步主specs |
| change/design.md | ADR、替代方案、取捨及連結，不複製第二份架構 |
| change/tasks.md | 1.x本次文件完成；2.x–4.x產品仍待做 |
| docs/refactor/traceability.md | RQ→需求ID→模組→scenario→任務→驗證 |

## 後續實作循環

先挑一項未勾選task與其依賴，讀對應scenario，再實作與測試，保存證據後才勾選。規格變動先更新proposal/spec/design與追蹤，不先修改測試集迎合結果。Codex已安裝 `openspec-propose`、`openspec-explore`、`openspec-apply-change`、`openspec-update-change`、`openspec-sync-specs`、`openspec-archive-change` 工作流程；實際名稱以 `.agents/skills/` 為準，可用自然語言指定工作。

目前不執行sync／archive。未來全部產品任務完成且審閱驗證後，才能使用 `openspec archive refactor-energy-proposal`；archive會更新主specs並移動change，不能用來表示「文件寫完」。新增不同範圍功能時先 `openspec new change <kebab-case-name>`，重複proposal/specs/design/tasks/validate循環。
