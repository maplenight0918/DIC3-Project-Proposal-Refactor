# 原始來源稽核與搜尋邊界

日期2026-11-13。沿用原研究A1–A5、D1–D9標記，實際回查原文；新增A6。搜尋式包括 `2026 building energy anomaly detection large language model agent paper` 及 `2026 building energy time series anomaly explanation LLM benchmark`。這是本課程提案的定向更新，不宣稱窮盡所有文獻或完成系統性回顧。

| Ref. | 本次閱讀原始位置 | 核對與修訂 | 可追溯入口 |
|---|---|---|---|
| A1 | arXiv v3方法、結果、失敗分析 | 動作—觀察循環；非建築效能依據 | [全文](https://arxiv.org/html/2210.03629v3) |
| A2 | arXiv v1架構、資料／評估設定 | 標註案例、規則融合、Event-F1 PA；不轉用作者提升率 | [全文](https://arxiv.org/html/2501.14170v1) |
| A3 | arXiv v1 §4與Table1 | 18序列；參數借助測試真值；降低誤報有漏報代價；以全文而非摘要的普遍語氣判讀 | [全文](https://arxiv.org/html/2503.21833v1) |
| A4 | LBNL原始PDF pp6–9（檔案頁碼）、Table1與討論 | 三題各五次、氣流下降3/5；成功不代表文字完整。PDF圖表及表下注腳一起讀 | [PDF](https://eta-publications.lbl.gov/sites/default/files/2025-07/extraction_and_analysis_of_time_series_data.pdf)、[DOI](https://doi.org/10.20357/B73W4C) |
| A5 | arXiv v1資料標註、實驗與附錄A限制 | AI回饋標註、主類型限制；頁首會議DOI仍為模板，不能推定正式出版 | [全文](https://arxiv.org/html/2507.15066v1) |
| A6 | arXiv v1 §II-A/E、III-A/D/E、IV | 七設備、16人工情境；動態取得的作者評分不是總表故障真值。消融僅稱開發中探索，未移植其效果量；作者稿自稱會議接受未獨立確認 | [全文](https://arxiv.org/html/2606.28467v1) |
| D1 | IEA Electricity demand之部門成長段 | 2025全球年增約3%，建築占年增近45%，非總量45% | [官方報告](https://www.iea.org/reports/global-energy-review-2026/electricity-demand) |
| D2 | 本次不重採用其49%預測數字 | 原文References保留為延伸閱讀；不作重構版論證必要證據，本次未重新核對此預測 | [官方入口](https://www.iea.org/reports/electricity-2026/demand) |
| D3 | 作者全文資料描述、建置及使用限制 | 1,636非住宅建築、3,053各類表、19場址、2016–2017逐時；不是3,053電表 | [作者全文](https://arxiv.org/html/2006.02273)、[出版DOI](https://doi.org/10.1038/s41597-020-00712-x) |
| D4/D5 | repository入口及LICENSE原文 | 固定下載入口與授權保留；沒有下載能源CSV，仍待鎖commit／檔案hash | [資料庫](https://github.com/buds-lab/building-data-genome-project-2)、[LICENSE](https://raw.githubusercontent.com/buds-lab/building-data-genome-project-2/master/LICENSE) |
| D6 | 官方wiki Raw/Cleaned/Kaggle全文 | raw逐時當地時間；cleaned將離群、特定長零值及電力零值換NaN；不直接移植清理假設成故障判定 | [資料說明](https://github.com/buds-lab/building-data-genome-project-2/wiki/Meters-data-features) |
| D7 | LBNL書目及完整PDF的摘要、方法與實務範圍 | 104組織、6,500建築是計畫母體；原3%/9%不作本專題預期節電。新稿只用實務流程與範圍 | [官方頁](https://bies.lbl.gov/publications/proving-business-case-building)、[報告PDF](https://eta-publications.lbl.gov/sites/default/files/kramer_provingbuildinganalytics_october2020.pdf)、[DOI](https://doi.org/10.20357/B7G022) |
| D8 | DOE FEMP官方A–D選項與whole-building說明 | 基準調整、個別措施不可由整棟測量直接分離；新稿作研究邊界推論 | [官方指南](https://www.energy.gov/cmei/femp/measurement-and-verification-options-federal-energy-and-water-saving-projects) |
| D9 | arXiv v1 §3.1、4.1–4.3、4.6 | SUSTIE、長上下文、微調與同棟區域；不稱跨建築故障驗證 | [全文](https://arxiv.org/html/2506.00630v1) |

作者結果、官方定義與本專題設計推論在正文分開。新增A6直接影響Research Gap與DQ3，不能再宣稱能源Agent或動態背景取得首次出現。沒有採用搜尋摘要中的未取得全文研究，不用年份湊文獻數。

## 存取限制及處理

教師GitHub一般頁初次失敗，改用GitHub官方API列目錄與raw讀README/課堂對話檔。OpenSpec官網在shell回403，但web工具可讀；另查官方v2.0.0 CLI文件與本機help，不用舊版opsx指令冒充現版。

LBNL網站在Python預設user-agent回403，但web可讀A4 PDF與D7官方書目。D7完整PDF超出web大小上限，改用curl下載原站PDF，以PyMuPDF發現內頁為影像，改檢視實際PDF頁面；沒有把摘要代替全文。原始全文暫存只作查核，不把整篇第三方論文再散布到提交包。

## 未核實事項

A5模板化會議書目及A6正式Xplore紀錄未獨立確認，僅引可讀arXiv版本。D2預測未重新核對且不使用。使用者情境尚無訪談；選定建築資料品質、模型版本、成本及研究效果尚無實測。DietSense的健康統計、資料量與成效目標不屬本專題證據，未核實、不引用、不移植；兩份解析PDF視為同一重複來源。
