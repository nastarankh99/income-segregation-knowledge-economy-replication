import pandas as pd
from linearmodels.iv import IV2SLS
import os

dataset_final = pd.read_csv("C:/Users/98910/Desktop/Replication- Econ 836- Nastaran Khorram/my_codes & final_dataset/final_dataset.csv")
os.makedirs("results_subsample", exist_ok=True)

median_income = dataset_final["log_income"].median()
low_income_df = dataset_final[dataset_final["log_income"] < median_income].dropna(subset=[
    "cz_nhh", "pat_growth", "pat_growth_instr", "segregation_diff",
    "college_share_90", "log_ncts", "log_nhh", "log_income", "d_tradeusch_pw", "state"
])

formula = (
    "segregation_diff ~ 1 + college_share_90 + log_ncts + log_nhh + log_income + d_tradeusch_pw "
    "+ [pat_growth ~ pat_growth_instr]"
)

iv_model = IV2SLS.from_formula(
    formula,
    data=low_income_df,
    weights=low_income_df["cz_nhh"]
).fit(cov_type="clustered", clusters=low_income_df["state"])

summary_df = pd.DataFrame({
    "coef": iv_model.params,
    "std_err": iv_model.std_errors,
    "t_stat": iv_model.tstats,
    "p_value": iv_model.pvalues
})
summary_df.to_csv("results_subsample/subsample_low_income_results.csv", index=False)

print(iv_model.summary)
with open("my_change.csv", "w") as f:
    f.write(iv_model.summary.as_csv())

sd_pat_growth = 0.499 #as mentioned in the paper, I didnt re-calculate it, since it comes from the same dataset
sd_segregation_diff = 2.12 #as mentioned in the paper, I didnt re-calculate it, since it comes from the same dataset
coef_subsample = iv_model.params["pat_growth"]

gini_point_effect = coef_subsample * sd_pat_growth
standard_dev_effect = gini_point_effect / sd_segregation_diff

print(f"IV coefficient on patent growth: {coef_subsample:.4f}")
print(f"Effect in Gini points: {coef_subsample:.4f} × {sd_pat_growth} = {gini_point_effect:.4f}")
print(f"Effect in SD units: {gini_point_effect:.4f} ÷ {sd_segregation_diff} = {standard_dev_effect:.4f}")