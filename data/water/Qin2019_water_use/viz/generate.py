#%%
import pandas as pd 
import altair as alt 

# Load the timeseries data
data = pd.read_csv('../processed/Qin2019_category_volume_1980-2016.csv')
data['year'] = pd.to_datetime(data['year'], format='%Y')

# %%
# Generate a vizualization for each category
for g, d in data.groupby(['category']):        
    domain_min = d['volume_km3'].values.min() - 10
    domain_max = d['volume_km3'].values.max() + 10
    chart = alt.Chart(d).encode(
                x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
                y=alt.Y(field='volume_km3', type='quantitative', title='volume [km³]',
                        scale=alt.Scale(domain=[domain_min, domain_max])),
                tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                         alt.Tooltip(field='volume_km3', type='quantitative', format='0.1f', title='volume [km³]')]
    ).properties(width='container', height=300)
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(color='dodgerblue', filled=True)
    layer = alt.layer(l, p)
    layer.save(f'./{g}.json')
# %%
# Generate a viz for the total water use
data = data.groupby(['year']).sum().reset_index()

chart = alt.Chart(data).encode(
                x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
                y=alt.Y(field='volume_km3', type='quantitative', title='volume [km³]',
                        scale=alt.Scale(domain=[1000, 1800])),
                tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                         alt.Tooltip(field='volume_km3', type='quantitative', format='0.1f', title='volume [km³]')]
        ).properties(width='container', height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('./total_volume.json')
layer

# %%
