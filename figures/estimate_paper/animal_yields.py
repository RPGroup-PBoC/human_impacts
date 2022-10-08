# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import anthro.viz
anthro.viz.plotting_style()


data = pd.read_csv(
    '../../data/agriculture/FAOSTAT_animal_product_yield/processed/FAOSTAT_animal_product_yield.csv')
data.head()

fig, ax = plt.subplots(1, 1, figsize=(6, 4))
for g, d in data.groupby(['animal', 'product']):
    d.sort_values('Year', inplace=True)
    if g[0] in ['chicken', 'pig', 'cow']:
        ax.plot(d['Year'], d['yield_kg_per_head'] /
                d['yield_kg_per_head'].values[0], '-', label=f'{g[0]} {g[1]}')
ax.legend()
ax.set_ylabel('fold increase in yield')
ax.set_xlabel('year')
plt.savefig('yield_test.pdf')
