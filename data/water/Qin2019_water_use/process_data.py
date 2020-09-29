#%%
import pandas as pd 

# Load the data
data = pd.read_csv('source/Fig1a_for_Griffin.csv')

# Melt on year
melted = data.melt('year')
melted.rename(columns={'variable':'subcategory', 'value':'volume_km3'}, inplace=True)

# Add coarse-grained categorizations. 
melted.loc[(melted['subcategory']=='reservoir'), 'category'] = 'reservoir',
melted.loc[(melted['subcategory']=='livestock') |
           (melted['subcategory']=='other_annuals') |
           (melted['subcategory']=='rice') |
           (melted['subcategory']=='maize') |
           (melted['subcategory']=='perennials') |
           (melted['subcategory']=='wheat'), 'category'] = 'agriculture'
melted.loc[(melted['subcategory']=='population'), 'category'] = 'domestic_municipal'
melted.loc[(melted['subcategory']=='thermal_power'), 'category'] = 'thermal_power'

# Save as a processed file. 
melted.to_csv('processed/Qin2019_subcategory_volume_1980-2016.csv',
               index=False)
        
# Compute the aggregate for all categories
categorized = melted.groupby(['category', 'year']).sum().reset_index()

categorized.to_csv('./processed/Qin2019_category_volume_1980-2016.csv', index=False)
# %%
# Compute the 2016 breakdowns. 
latest = melted[melted['year']==2016]

# Define a dictionary of the breakdown for each category. 
cat = {'reservoir': {
            'hydroelectric':0.69,
            'irrigation':0.14,
            'flood_control':0.08,
            'water_supply':0.01,
            'other':0.08},
       'thermal_power': {
            'coal': 0.54,
            'nuclear': 0.15,
            'waste_heat': 0.14,
            'gas': 0.07,
            'biomass':0.04,
            'oil':0.03,
            'other':0.03},
        'livestock':{
            'cattle':0.8,
            'pig': 0.08,
            'sheep': 0.06,
            'other':0.06},
        'perennials': {
            'other_perennials': 0.71,
            'citrus':  0.19,
            'date_palm':0.08,
            'coffee': 0.01},
        'other_annuals': {'other': 1},
        'population': {'population':1},
        'wheat': {'wheat':1},
        'maize': {'maize':1},
        'rice': {'rice':1}}

# Set up a new dataframe.
breakdown_df = pd.DataFrame({})
for k, v in cat.items():
    d = latest[latest['subcategory']==k]
    total_vol = d['volume_km3'].values[0]
    if k in ['perennials', 'other_annuals', 'wheat', 'maize', 'rice']:
        cat = 'agriculture'
    for _k, _v in v.items():
        print(k)
        if _k == 'hydroelectric':
            cat = 'hydroelectric_power'
        elif _k == 'population':
            cat = 'domestic/municipal'
        elif k  in ['perennials', 'other_annuals', 'wheat', 'maize', 'rice']:
            cat = 'agriculture'
        else:
            cat = k
        breakdown_df = breakdown_df.append({
            'year': 2016,
            'category': cat,
            'subcategory': _k,
            'volume_km3': total_vol * _v},
            ignore_index=True)
breakdown_df['year'] = breakdown_df['year'].astype(int)

# Save to a csv. 
breakdown_df.to_csv('./processed/Qin2019_subcategory_volume_breakdown_2016.csv',
                    index=False)
# %%
# Compute a more coarse-grained breakdown of the 2016 values.
grouped = breakdown_df.groupby(['category', 'year']).sum().reset_index()
grouped.to_csv('./processed/Qin2019_category_volume_breakdown_2016.csv', index=False)

# %%


# %%
