#%%
import numpy as np
import pandas as pd
data = pd.read_csv('./processed/IUCN_class_order_extinctions.csv')
bg_rate = 2 # E / MSY
years = 520 # since 1500
expected_per_10k_per_c = bg_rate * years/100

# Melt on kingdom and name
melted = data.melt(['kingdom', 'class_order'], var_name='assessment', value_name='number')
melted['number'] = melted['number'].astype(int)
melted.to_csv('./processed/IUCN_class_order_extinctions_tidy.csv', index=False)

# Compute the expected extinctions for each kingdom.
expected = {g: d[d['assessment']=='total_species_assessed']['number'].sum() * expected_per_10k_per_c  / 1E4 for g, d in melted.groupby(['kingdom'])}
expected

# Exclude totals numbers
melted = melted[melted['assessment']!= 'total_species_assessed']

# Compute the totals for each assessment.
by_assessment = melted.groupby(['kingdom', 'assessment']).sum().reset_index()
by_assessment.to_csv('./processed/IUCN_kingdom_by_assessment.csv')

# Create different assessment catagories
cats = {'highly conservative (extinct only)': ['extinct'],
        'conservative (extinct or extinct in wild)': ['extinct', 'extinct_in_wild'],
        'moderate (extinct or probably extinct)': ['extinct', 'probably_extinct'],
        'permissive (extinct, probably extinct, extinct in wild, probably extinct in wild)':
                ['extinct', 'probably_extinct', 'extinct_in_wild', 'probably_extinct_in_wild']}

cat_df = pd.DataFrame([])
for g, d in melted.groupby(['kingdom']):
    for k, v in cats.items():
        _d = d[d['assessment'].isin(v)]
        n_species = _d['number'].sum()
        cat_df = cat_df.append({'kingdom':g,
                                'definition': k,
                                'observed': n_species,
                                'expected': expected[g]},
                                ignore_index=True)

cat_df['observed'] = cat_df['observed'].astype(int)
cat_df['extinction_foldchange'] = cat_df['observed'].values / cat_df['expected'].values
cat_df['bg_rate_EMSY'] = bg_rate
cat_df.to_csv('./processed/IUCN_kingdom_extinction_expectations.csv', index=False)
# %%
cat_df

# %%
