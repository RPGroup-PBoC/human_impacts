# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import anthro.viz
import tqdm
import growth.viz
# cor = anthro.viz.plotting_style()
cor, pal = growth.viz.matplotlib_style()

# %%
# Load the livestock population data.
data = pd.read_csv(
    '../../data/agriculture/FAOSTAT_livestock_population/processed/FAOSTAT_livestock_population.csv')
animals = ['cattle', 'chickens', 'pigs', 'sheep']
data = data[data['animal'].isin(animals)]
pop_data = pd.read_csv(
    '../../data/anthropocentric/FAOSTAT_world_population/processed/FAOSTAT_total_population.csv')
pop_data.rename(columns={'Year': 'year'}, inplace=True)
merged = data.merge(pop_data, on='year')

# %%
yields = pd.read_csv(
    '../../data/agriculture/FAOSTAT_livestock_product_produced/processed/FAOSTAT_livestock_and_product.csv')
yields.rename(columns={'Year': 'year'}, inplace=True)
yield_merge = yields.merge(pop_data, on='year')

# %%
fig, ax = plt.subplots(1, 1)
for g, d in yields.groupby(['subcategory']):
    if g != 'egg':
        ax.plot(d['year'], d['yield_kg_per_head'] / d['yield_kg_per_head'].min(),
                label=g)
ax.legend()
ax.set_xlabel('year')
ax.set_ylabel('fold increase in yield')
plt.savefig('./yields.pdf')
# %%
n_draws = int(1E4)
_pop = pop_data[pop_data['year'] >= 1961]
pop_range = np.linspace(_pop['population'].min(),
                        _pop['population'].max(), 200)
year_range = np.linspace(1961, 2018, len(pop_range))
rho = 3000
M = 150 * (1 + 0.01 * (year_range - 1961))
phi = 0.03
E = 3E3 * 365  # Assuming 2000 kcal / day / person
tau = 4.5
# M = np.sqrt(np.random.normal(M_mu, M_sig, n_draws)**2)
# tau = np.sqrt(np.random.normal(tau_mu, tau_sig, n_draws)**2)
# phi = np.sqrt(np.random.normal(phi_mu, phi_sig, n_draws)**2)
beef_cattle_yield = tau * pop_range * (phi * E) / (rho * M)
beef_cattle_noyield = tau * pop_range * (phi * E) / (rho * 250)
beef_cattle_point = tau * pop_range[-1] * (phi * E) / (rho * 250)

# %%
fig, ax = plt.subplots(1, 1, figsize=(1.5, 1.5))
# ax.set_xscale('log')
# ax.set_yscale('log')
# milk_cattle = tau * pop_range * (phi * E)/(rho * M)
cows = merged[merged['animal'] == 'cattle']
ax.plot(cows['population']/1E9, cows['population_Mhd']
        * 1E6/1E9, 'o', color=cor['light_black'], ms=3.5,
        markeredgecolor='k', markeredgewidth=0.25)
# ax.plot(cows['population'].values[-1] / 1E9, cows['population_Mhd'].values[-1] * 1E6 / 1E9, 'o', color=cor['red'], label='data')

# Yield
ax.plot(pop_range/1E9, beef_cattle_yield/1E9,
        '-', color=cor['light_blue'], lw=1)
# label='estimate')  # + milk_cattle)

# No yield
# ax.plot(pop_range/1E9, beef_cattle_noyield/1E9, 'k--',
# label='estimate')

# Point Estimate
# ax.hlines(beef_cattle_point/1E9, pop_range[0]/1E9, pop_range[-1] /
#   1E9, color='k', linestyle='--', label='estimate', linewidth=1)
ax.set_ylim([0.95 * cows['population_Mhd'].min() * 1E6 / 1E9, 1.6])
ax.set_yticks([1, 1.3, 1.6])
ax.set_xticks([4, 6, 8])
# ax.set_xticks([7.5])
# ax.set_xlabel('human population [billions]')
# ax.set_ylabel('cattle population [billions]')
# ax.legend(loc='lower right')
plt.tight_layout()
plt.savefig('./cattle_estimate_noyield.pdf', bbox_inches='tight')

# %%


# %%
# Try for chickens and pigs
rho = 3000
M = 1 * (1 + 0.01 * (year_range - 1961))
phi = 0.05 * (1 + 0.05 * (year_range - 1961))
E = 3E3 * 365  # Assuming 2000 kcal / day / person
tau = 0.1
chicken_yield = tau * pop_range * (phi * E) / (rho * M)
plt.plot(pop_range/1E9, chicken_yield/1E9, 'k--')
chicken = merged[merged['animal'] == 'chickens']
plt.plot(chicken['population'] / 1E9,
         chicken['population_Mhd'] * 1E6 / 1E9, '-o')
plt.ylabel('chicken population [billions]')
plt.xlabel('human population [billions]')
plt.savefig('./chicken_yield_change.pdf')

# %%
rho = 3000
M = 60 * (1 + 0.01 * (year_range - 1961))
phi = 0.1
E = 3E3 * 365  # Assuming 2000 kcal / day / person
tau = 0.5
pig_yield = tau * pop_range * (phi * E) / (rho * M)
swine = merged[merged['animal'] == 'pigs']
plt.plot(swine['population'] / 1E9,
         swine['population_Mhd'] * 1E6 / 1E9, '-o', color=cor['purple'], label='data')
plt.plot(pop_range/1E9, pig_yield/1E9, 'k--', label='estimate')
plt.xlabel('human population [billions]')
plt.ylabel('pig population [billions]')
plt.savefig('./pig_yield_estimate.pdf')
# %%
