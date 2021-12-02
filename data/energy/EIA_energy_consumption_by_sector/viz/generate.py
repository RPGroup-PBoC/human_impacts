#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for sectorial energy consumption (TW) from EIA International Outlook
data = pd.read_csv('../processed/Passenger_transportation_energy_use.csv')
data['Year'] = pd.to_datetime(data['Year'].astype(str), format='%Y', errors='coerce')

targets = ['Passenger light-duty vehicles',
            'Passenger air transport',
            'Total passenger transport']
target_domains = [[1.1, 1.7], [0.1, 0.6], [1.4, 2.6]]
for target, domain in zip(targets, target_domains):
   agg_data = pd.DataFrame()
   agg_data['Year'] = (data[data['Reported sector']==target])['Year']
   agg_data['Energy consumption (TW)'] = (data[data['Reported sector']==target])['Energy consumption (TW)']

   chart = alt.Chart(agg_data).encode(
               x=alt.X(field='Year', type='temporal', timeUnit='year', title='Year'),
               y=alt.Y(field='Energy consumption (TW)', type='quantitative', title=target+' consumption (TW)',
                   scale=alt.Scale(domain=domain)),
               tooltip=[alt.Tooltip(field='Year', type='temporal', title='Year', format='%Y'),
                        alt.Tooltip(field=r'Energy consumption (TW)', type='nominal', title=r'Energy consumption (TW)')]
               ).properties(width='container', height=300)

   l = chart.mark_line(color='dodgerblue')
   p = chart.mark_point(color='dodgerblue', filled=True)
   layer = alt.layer(l, p)
   target_machine_readable = ('_').join(target.split(' '))
   layer.save(target_machine_readable+'.json')

