# DIC3最終驗收紀錄

驗收日期：2026-11-13。專案：第25組 Energy Detective。工作範圍為提案重構、設計規格化及Proposal簡報；本紀錄不代表產品功能或能源實驗完成。

## 五項課堂任務

| 任務 | 本次交付與驗收結果 |
|---|---|
| 安裝OpenSpec、理解spec-driven development | 真實安裝2.0.0，CLI init生成Codex技能與config，建立active change，完成proposal→specs/design→tasks及嚴格驗證；[操作文件](workflow.md)可重現 |
| A–F與5／3／10 | [完整提案](../../research/proposal_refactored.md)包含六段摘要、299字整合摘要及英文版本、5個思維模式、3個有證據的爭論／工程取捨、10題推理與設計影響 |
| DESIGN轉OpenSpec | 主設計保留唯一技術編輯來源；五個擬議能力、14項產品需求、36個情境及[追蹤矩陣](traceability.md)；主spec只記錄既有文件工具 |
| Introduction refactor | 連貫文章涵蓋G–L，客觀證據區分統計母體，明確定義使用者、問題、限制與可驗證貢獻 |
| Related Work refactor | 6篇AI與6份領域核心來源按問題分類、8欄Article Summary Table、2025–2026研究及經典資料、Research Gap；引用可回查，未宣稱系統性文獻回顧 |

## 依正式規範權重檢查（不是自行給分）

| 評分項目 | 比例 | 可檢查證據 | 判定／限制 |
|---|---:|---|---|
| Introduction | 20% | 提案§2，客觀需求、研究問題與G–L對應 | 文件完成；沒有把Agent串接本身稱為創新 |
| Related Work | 20% | 提案§3、§8及[source-audit](source-audit.md) | 分類比較與來源查核完成；預印本版本、未獨立核實出版狀態明示 |
| Deep Research | 20% | 提案§4的M1–M5、DQ1–DQ3、Q01–Q10 | 概念／證據／限制／設計影響、雙方論點、參考回答齊備 |
| Proposed AI Agent與Architecture | 20% | 提案§5、[DESIGN](../../DESIGN.md)、八模組圖與介面表 | 設計完成；Agent與資料分析程式尚未實作 |
| Flowchart、Pseudocode、技術可行性 | 15% | 完整流程分支與44行偽碼、評估協議、36情境 | 設計與呈現完成；錯誤／降級／預算／保存已對齊，尚未執行產品情境測試 |
| GitHub、DESIGN與完整度 | 5% | 既有Git repository、README入口、A2Z、OpenSpec及原檔雜湊 | 文件交付完成；使用者後續已授權提交至DIC3遠端，最新提交檢查見github-submission-check.md |

[A2Z對應表](a2z.md)沿用附件原定義；U／V／Y呈現規劃與預期成果，沒有補造實驗。PA–PM也核對，PM形式證明對本系統不適用並說明。

## 實際命令與結果

執行環境：Node v22.20.0、npm 10.9.3、OpenSpec 2.0.0；Python文件環境沿用既有`.build-deps`。OpenSpec要求Node >=22.12.0，本環境符合。圖表使用Mermaid CLI 11.12.0及本機Chrome；所有生成來源納入提交。

| 實際命令（專案根目錄） | 結果 |
|---|---|
| `npm install --global @fission-ai/openspec@2.0.0` | 安裝成功；`openspec --version`回傳2.0.0 |
| `OPENSPEC_TELEMETRY=0 openspec init --tools codex --language '繁體中文' --no-animation` | 成功初始化，產生config及六個Codex skills |
| `OPENSPEC_TELEMETRY=0 openspec new change refactor-energy-proposal` | 成功建立spec-driven變更，已依各artifact指引完成內容 |
| `.build-deps/bin/python scripts/build_refactor.py` | 成功產生重構HTML、27頁可編輯PPTX、PDF與逐頁稿，原Proposal未覆寫 |
| `.build-deps/bin/python scripts/verify_refactor.py` | 通過530項文件一致性檢查：14項需求、36情境、27頁、299字；逐項結果見[document-validation.json](document-validation.json) |
| `.build-deps/bin/python scripts/verify_deliverables.py` | 原29頁簡報、DOCX/PPTX XML、PDF界限與原文件檢查通過 |
| `OPENSPEC_TELEMETRY=0 openspec validate --all --strict --no-interactive --json` | 2項（1個main spec、1個change）全部通過，0問題；見[JSON](openspec-validation.json) |
| `OPENSPEC_TELEMETRY=0 openspec doctor --json` | healthy=true，見[診斷](openspec-doctor.json) |
| `openspec status --change refactor-energy-proposal --json` | 四類規劃artifact齊備，見[status](openspec-status.json)；不代表產品完成 |
| `openspec instructions apply --change refactor-energy-proposal --json` | 只讀取狀態／指引；本次文件6項完成，產品12項未完成，見[apply狀態](openspec-apply-status.json) |
| `git diff --check` | 無空白或衝突標記問題 |
| `.build-deps/bin/python scripts/package_refactor.py` | 產生提交ZIP並驗證所有檔案SHA-256；清單見[manifest](submission-manifest.json) |

第一輪命令stdout、stderr與退出碼保存在[commands.log](commands.log)。安裝與初始化為前面已完成的操作，不為收集log而重跑。`instructions apply`不會執行產品，本次沒有apply產品、sync產品spec或archive。

## 呈現與內容檢查

- 已檢視正式規範與A2Z頁面、DietSense資訊圖表、原專案技術圖及必要研究原文表格；兩份教學解析PDF文字相同，分類為重複教學內容。
- 已檢視新版全部27頁PDF縮圖，以及架構、流程、偽碼等技術頁放大畫面。架構頁改為可編輯八模組總覽，複雜流程拆成三頁，避免縮小整張長圖造成字體無法閱讀；完整圖仍保留於DESIGN與HTML。
- HTML以Chrome實際載入檢查，1440 px視窗沒有水平溢出，兩張圖都載入、14張表完整；實際查看摘要及Article Summary Table畫面。已修正相鄰Markdown引用誤解析，並加入自動檢查。
- PPTX ZIP／XML／relationships可解析，27頁皆有備註，44行偽碼與DESIGN一致；文字框及PDF文字界限檢查通過。圖解頁的備註與完整逐頁稿含對應Mermaid內容。
- PDF是由同一簡報來源、字體與座標繪製的可攜預覽，**不是Microsoft PowerPoint原生匯出的結果**。環境沒有原生Office；不同電腦開啟PPTX的字型替代與換行仍應由提交者快速檢視。PDF內嵌CJK字型可作為穩定閱讀版本。
- 原有23個受Git追蹤檔案的起始hash已保存；只有授權更新的README、DESIGN、.gitignore有修改，其餘20個原檔hash一致。原始Proposal DOCX／PPTX／PDF、研究稿、圖及工具均保留。

## 閱讀、重建與提交

1. 從[README](../../README.md)進入完整提案與新版簡報。瀏覽器版需保留相對目錄，不能只複製單獨HTML。
2. 一般文件修改後執行build_refactor與verify_refactor；若修改技術圖，依README重新渲染Mermaid。主要技術在DESIGN編輯，評估在research/refactor/evaluation.md編輯；Proposal標記區由建置同步。
3. 重跑OpenSpec strict validate，再執行`python scripts/package_refactor.py`。ZIP位於`deliverables/refactor/submission.zip`，包含來源、原版與新版交付、規格與驗收紀錄，不含.git、Python/Node環境、真實原始資料、課堂附件或研究全文暫存。
4. ZIP內檔案可依submission-manifest.json驗SHA-256；已實際解壓至獨立暫存目錄、逐檔驗hash，並使用既有Python套件環境在解壓目錄通過新版514項檢查與原版檢查。未測全新電腦安裝依賴；解壓後以README指令重建。ZIP本體為生成檔已列gitignore，提交原始碼時保留其生成腳本與清單即可。
5. 第一輪依要求沒有推送；後續依使用者授權提交DIC3指定遠端，見[提交前核對](github-submission-check.md)。老師只收附件時可直接交ZIP，或交新版Proposal、PPTX/PDF並附完整來源。

## 未完成項目與驗收界線

目前沒有能源Agent、BDG2本地資料、標註、產品測試或實測結果。資料切分、樣本數與成功判準均為設計設定，沒有借用DietSense範例成效。產品功能12項保持未勾選；不能因OpenSpec檔案結構通過而宣稱場景通過。

後續需確定單棟建築及期間、資料版本／授權、LLM供應者與固定版本／預算、兩位標註者與實際規則適用性。A5及A6的正式出版狀態尚未獨立確認，故僅引用已讀預印本；D2保留為原稿延伸資料但本次未重查、未作論證依據。其餘查核範圍與限制見[source-audit](source-audit.md)，不是完全無限制的引用背書。

完整產品、正式實驗、Final PPT >20頁、影片 >10分鐘及正式Final結論列為後續交付。A4橫式資訊圖表是選配，本次未製作。詳細缺項與修訂理由見[revisions-and-next](revisions-and-next.md)。
