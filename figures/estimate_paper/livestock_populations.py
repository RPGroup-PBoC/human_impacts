# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import anthro.viz
import tqdm
cor = anthro.viz.plotting_style()

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
pop_range = np.linspace(3, 8, 200) * 1E9
rho = 3000
M_mu = 250
M_sig = 10
phi_mu = 0.03
phi_sig = 0.02
E = 3E3 * 365  # Assuming 2000 kcal / day / person
tau_mu = 4
tau_sig = 1
M = np.sqrt(np.random.normal(M_mu, M_sig, n_draws)**2)
tau = np.sqrt(np.random.normal(tau_mu, tau_sig, n_draws)**2)
phi = np.sqrt(np.random.normal(phi_mu, phi_sig, n_draws)**2)

cattle_df = pd.DataFrame()
for i in tqdm.tqdm(range(n_draws)):
    beef_cattle = tau[i] * pop_range * (phi[i] * E)/(rho * M[i])
    _df = pd.DataFrame(np.array([beef_cattle]).T, columns=['N'])
    _df['H'] = pop_range
    _df['sample'] = i
    cattle_df = pd.concat([cattle_df, _df])
# %%
Y = 1 + 0.03 * (d['year'] - 1960)
# %%
cattle_stats = pd.DataFrame([])
percs = [(0.25, 97.5), (12.5, 87.25), (25, 75),  (37.5, 62.5), (47.5, 52.5)]
perc_labels = ["95%", "75%", "50%", "25%", "5%"]
for g, d in cattle_df.groupby(['H']):
    for i, p in enumerate(percs):
        _percs = np.percentile(d['N'], p)
        _df = pd.DataFrame([perc_labels[i], _percs[0], _percs[1], g]).T
        _df.columns = ['percentile', 'low', 'high', 'H']
        cattle_stats = pd.concat([cattle_stats, _df], sort=False)


# %%
fig, ax = plt.subplots(1, 1, figsize=(4, 4))
# for g, d in cattle_df.groupby(['sample']):
#     if g % 2 == 0:
#         ax.plot(d['H'], d['N'], 'k-', lw=0.1, alpha=0.75)
for g, d in cattle_stats.groupby(['percentile']):
    ax.fill_between(d['H'].values.astype(float), d['low'].values.astype(float), d['high'].values.astype(float),
                    alpha=0.1, color='k')

ax.set_xscale('log')
ax.set_yscale('log')
# milk_cattle = tau * pop_range * (phi * E)/(rho * M)
cows = merged[merged['animal'] == 'cattle']
ax.plot(cows['population'], cows['population_Mhd']
        * 1E6, '-o', color=cor['red'], ms=5)
# ax.plot(pop_range, beef_cattle)  # + milk_cattle)
ax.set_xticks([3E9, 5E9, 7E9])
# %%
fig, ax = plt.subplots(1, 1, figsize=(3, 3))
for g, d in merged.groupby(['animal']):
    ax.plot(d['population'], d['population_Mhd'] * 1E6, '-o', label=g)
ax.legend()
ax.set_yscale('log')
ax.set_ylim([1E8, 5E10])

# %%
