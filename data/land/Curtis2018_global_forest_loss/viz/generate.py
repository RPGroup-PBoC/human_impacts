#%%
import pandas as pd 
import anthro.io
import altair as alt

data = pd.read_csv('../processed/Curtis2018_deforestation_timeseries.csv')
data.head()
#%%
data['year'] = pd.to_datetime(data['year'], format='%Y')
data['area'] = anthro.io.numeric_formatter(data['area_Mha'].values *1E6, sci=False, unit='ha')

chart =  alt.Chart(data).encode(
        x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
        y=alt.Y(field='area_Mha', type='quantitative', title='commodity-driven deforestaion [Mha]',
                scale=alt.Scale(domain=[2, 8])),
                tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                 alt.Tooltip(field='area', type='nominal', title='deforested area')]
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')    
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('deforested_area.json')

# %%
