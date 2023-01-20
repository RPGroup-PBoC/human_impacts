# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import anthro.viz
anthro.viz.plotting_style()
pal = anthro.viz.color_palette()

data = pd.read_csv(
    '../../data/agriculture/FAOSTAT_animal_product_yield/processed/FAOSTAT_animal_product_yield.csv')
data.head()
cor = {'chicken eggs': pal['light_blue'],
       'chicken meat': pal['blue'],
       'cow meat': pal['red'],
       'cow milk': pal['light_red'],
       'pig meat': pal['purple']}
fig, ax = plt.subplots(1, 1, figsize=(7, 4))
for g, d in data.groupby(['animal', 'product']):
    d.sort_values('Year', inplace=True)
    if g[0] in ['chicken', 'pig', 'cow']:
        ax.plot(d['Year'], d['yield_kg_per_head'] / d['yield_kg_per_head'].values[0],
                '-', label=f'{g[0]} {g[1]}', color=cor[f'{g[0]} {g[1]}'],
                lw=2)
# Plot the simplistic description
year_range = np.linspace(1960, 2020, 100)
fit = 1 + 0.007 * (year_range - 1960)
ax.plot(year_range, fit, 'k--', label="≈ 1% increase per year")
ax.legend()
ax.set_ylabel('fold increase in yield')
ax.set_xlabel('year')
plt.savefig('animal_yields_fit.pdf')
# %%
fig, ax = plt.subplots(1, 1, figsize=(7, 4))
for g, d in data.groupby(['animal', 'product']):
    d.sort_values('Year', inplace=True)
    if (g[0] == 'cow') & (g[1] == 'meat'):
        ax.plot(d['Year'], d['yield_kg_per_head'] / d['yield_kg_per_head'].values[0],
                '-', label=f'{g[0]} {g[1]}', color=cor[f'{g[0]} {g[1]}'],
                lw=2)
ax.legend()
ax.set_ylabel('fold increase in yield')
ax.set_xlabel('year')
plt.savefig('cow_relative_yields.pdf')

# %%
fig, ax = plt.subplots(1, 1, figsize=(7, 4))
for g, d in data.groupby(['animal', 'product']):
    d.sort_values('Year', inplace=True)
    if (g[0] == 'cow') & (g[1] == 'meat'):
        ax.plot(d['Year'], d['yield_kg_per_head'],
                '-', label=f'{g[0]} {g[1]}', color=cor[f'{g[0]} {g[1]}'],
                lw=2)
ax.legend()
ax.set_ylabel('yield [kg beef / cow]')
ax.set_xlabel('year')
plt.savefig('cow_total_yields.pdf')

# %%
# All animal total yields
fig, ax = plt.subplots(1, 1, figsize=(7, 4))
for g, d in data.groupby(['animal', 'product']):
    if g[0] in ['chicken', 'pig', 'cow']:
        if g[1] != 'milk':
            d.sort_values('Year', inplace=True)
            ax.plot(d['Year'], d['yield_kg_per_head'],
                    '-', label=f'{g[0]} {g[1]}', color=cor[f'{g[0]} {g[1]}'],
                    lw=2)
ax.legend()
ax.set_ylabel('yield [kg product / cow]')
ax.set_xlabel('year')
# ax.set_yscale('log')
plt.savefig('animal_total_yields.pdf')
