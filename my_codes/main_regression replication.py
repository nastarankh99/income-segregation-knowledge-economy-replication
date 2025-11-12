import os
import pandas as pd
from linearmodels.iv import IV2SLS

dataset_final = pd.read_csv("C:/Users/98910/Desktop/Replication- Econ 836- Nastaran Khorram/my_codes & final_dataset/final_dataset.csv")

dataset_final = dataset_final.dropna(subset=["segregation_diff", "pat_growth", "pat_growth_instr",
                                             "college_share_90", "log_ncts", "log_nhh", "log_income",
                                             "d_tradeusch_pw", "state", "cz_nhh"])

formula = "segregation_diff ~ 1 + college_share_90 + log_ncts + log_nhh + log_income + d_tradeusch_pw + [pat_growth ~ pat_growth_instr]"

ivmod = IV2SLS.from_formula(
    formula,
    data=dataset_final,
    weights=dataset_final["cz_nhh"]
).fit(cov_type="clustered", clusters=dataset_final["state"])

print(ivmod.summary)
with open("my_replication_result_table2_col6.csv", "w") as f:
    f.write(ivmod.summary.as_csv())


sd_pat_growth = 0.499  #as mentioned in the paper, I didnt re-calculate it, since it comes from the same dataset
sd_segregation_diff = 2.12 #as mentioned in the paper, I didnt re-calculate it, since it comes from the same dataset
coef = ivmod.params["pat_growth"]


gini_point_increase = coef * sd_pat_growth
standard_deviation_effect = gini_point_increase / sd_segregation_diff

print(f"IV coefficient on patent growth: {coef:.4f}")
print(f"Effect in Gini points: {coef:.4f} × {sd_pat_growth} = {gini_point_increase:.4f}")
print(f"Effect in SD units: {gini_point_increase:.4f} ÷ {sd_segregation_diff} = {standard_deviation_effect:.4f}")
