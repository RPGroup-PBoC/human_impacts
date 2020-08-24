#%%
import numpy as np
import pandas as pd
YEAR_WINDOW = 400 # Years considered for human era

# Load the data 
data = pd.read_csv('./processed/IUCN_extinction_numbers.csv')

# Restrict data only to animalia and plantae, for which we have a better idea 
# of the background extinction rate. 
data = data[(data['kingdom']=='animalia') | (data['kingdom']=='plantae')]

# Assign the background extinction rates based on kingdom. 
data.loc[data['kingdom']=='animalia', 'background_ex_rate'] = 0.1
data.loc[data['kingdom']=='plantae', 'background_ex_rate'] = 0.1
data.loc[data['phylum']=='chordata', 'background_ex_rate'] = 2

# Compute the extinction rate. 
data['extinction_rate_msy'] = data['subtotal_extinct'].values / YEAR_WINDOW / data['total_species'].values * 1E6
data['extinction_fold_change'] = data['extinction_rate_msy'].values / data['background_ex_rate'].values

# Chordates
chordates = data[data['phylum']=='chordata'].groupby('phylum').agg(('sum')).reset_index()
chordates['extinction_rate_msy'] = chordates['subtotal_extinct'].sum() / YEAR_WINDOW / chordates['total_species'].values.sum() * 1E6
chordates['fold_change'] = chordates['extinction_rate_msy'].values / 2

# Invertebrates
inverts = data[(data['kingdom']=='animalia') & (data['phylum']!='chordata')].groupby('kingdom').agg(('sum')).reset_index()
inverts['extinction_rate_msy'] = inverts['subtotal_extinct'].sum() / YEAR_WINDOW / inverts['total_species'].values.sum() * 1E6
inverts['fold_change'] = inverts['extinction_rate_msy'].values / 0.1 

# Plants
plants = data[data['kingdom']=='plantae'].groupby('kingdom').agg(('sum')).reset_index()
plants['extinction_rate_msy'] = plants['subtotal_extinct'].sum() / YEAR_WINDOW / plants['total_species'].values.sum() * 1E6
plants['fold_change'] = plants['extinction_rate_msy'].values / 2
plants





# %%
chordates
# %%
