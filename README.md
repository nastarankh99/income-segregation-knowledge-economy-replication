
# Income Segregation & the Knowledge Economy - Replication (Berkes & Gaetani, 2023)

This is my ECON 836 - Applied Econometrics replication of **“Income Segregation and the Rise of the Knowledge Economy” (Berkes & Gaetani, 2023)**.  
I re-run the main IV result and a low-income robustness check.

## What’s here
- `my_report/` — my write-up (PDF)
- `my_results` — CSV & figures - regression outputs
- `my_codes` — my scripts (IV+robustness)
- `data/` — empty; please refer to the AEA (American Economic Association) website to download article's replication package and data. https://www.aeaweb.org/articles?id=10.1257/app.20210074
-  `article/` — original article file (PDF)

## Environment
```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt


## Results
my_replication_result_table2_col6.csv (main IV replication)
my_change_in_sample_result.csv (robustness check, only considered low-income cities)
my_replication_figure_scatter_weighted_corrected.pdf

