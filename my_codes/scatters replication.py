import matplotlib.pyplot as plt
import numpy as np
from matplotlib import ticker
import os
import pandas as pd
import statsmodels.api as sm

dataset_final = pd.read_csv("C:/Users/98910/Desktop/Replication- Econ 836- Nastaran Khorram/my_codes & final_dataset/final_dataset.csv")
os.makedirs("figures", exist_ok=True)


def setup(ax):
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_major_locator(ticker.AutoLocator())
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(which='major', width=1.00)
    ax.tick_params(which='major', length=4)

def weighted_line(x, y, weights):
    x_array = np.array(x)
    x_design = sm.add_constant(x_array)
    model = sm.WLS(y, x_design, weights=weights).fit()
    x_pred = np.linspace(x_array.min(), x_array.max(), 100)
    x_pred_design = sm.add_constant(x_pred)
    y_pred = model.predict(x_pred_design)
    return x_pred, y_pred, model.params


cz_nhh = dataset_final["cz_nhh"]
pat_growth = dataset_final["pat_growth"]
segregation_diff = dataset_final["segregation_diff"]
dissim_occ_diff = dataset_final["dissim_occ_diff"]
dissim_edu_diff = dataset_final["dissim_edu_diff"]


fig, axs = plt.subplots(1, 3, figsize=(22, 5.2))

axs[0].scatter(pat_growth, segregation_diff, s=[pop/3000 for pop in cz_nhh],
               facecolors='none', edgecolors='b', alpha=0.5, linewidths=0.5)
x_line, y_line, _ = weighted_line(pat_growth, segregation_diff, cz_nhh)
axs[0].plot(x_line, y_line, color='purple', linewidth=2)
axs[0].set_xlabel('Patenting growth', fontsize=16)
axs[0].set_ylabel(r'$\Delta \, IncSegr$', fontsize=16)
axs[0].set_title("Figure 3A: Income Segregation", fontsize=14)
setup(axs[0])

axs[1].scatter(pat_growth, dissim_occ_diff, s=[pop/3000 for pop in cz_nhh],
               facecolors='none', edgecolors='b', alpha=0.5, linewidths=0.5)
x_line, y_line, _ = weighted_line(pat_growth, dissim_occ_diff, cz_nhh)
axs[1].plot(x_line, y_line, color='purple', linewidth=2)
axs[1].set_xlabel('Patenting growth', fontsize=16)
axs[1].set_ylabel(r'$\Delta \, OccSegr$', fontsize=16)
axs[1].set_title("Figure 3B: Occ. Segregation", fontsize=14)
setup(axs[1])

axs[2].scatter(pat_growth, dissim_edu_diff, s=[pop/3000 for pop in cz_nhh],
               facecolors='none', edgecolors='b', alpha=0.5, linewidths=0.5)
x_line, y_line, _ = weighted_line(pat_growth, dissim_edu_diff, cz_nhh)
axs[2].plot(x_line, y_line, color='purple', linewidth=2)
axs[2].set_xlabel('Patenting growth', fontsize=16)
axs[2].set_ylabel(r'$\Delta \, EduSegr$', fontsize=16)
axs[2].set_title("Figure 3C: Edu. Segregation", fontsize=14)
setup(axs[2])


plt.tight_layout()
plt.savefig("figure_scatter_weighted_corrected.pdf")
plt.show()