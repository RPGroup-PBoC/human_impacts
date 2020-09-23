#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Load the produciton data. 
data = pd.read_csv('../processed/Geyer2017_plastic_production.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')

chart = alt.Chart(data).encode(
            x=alt.X(field='year', timeUnit='year', title='year'),
            y=alt.Y(field='resin_production_Mt', type='quantitative',
                    title='')
)
# %%
