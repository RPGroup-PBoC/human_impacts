#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate a plot for fuel economy of all US light-duty vehicles
data = pd.read_csv('../processed/tidy_automotive_trends.csv')
data = data[(data['Reported quantity']=='Real-world fuel economy (MPG)') & (data['Regulatory Class']=='All')]
agg_data = pd.DataFrame()
agg_data['Year'] = data['Model Year']
agg_data['Fuel economy'] = round(data['Reported value']/2.352, 3)

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='Year', type='quantitative', title='Year'),
            y=alt.Y(field=r'Fuel economy', type='quantitative', title=r'Fuel economy (km/L)',
                scale=alt.Scale(domain=[5, 12])),
            tooltip=[alt.Tooltip(field='Year', type='quantitative', title='Year'),
                     alt.Tooltip(field=r'Fuel economy', type='quantitative', title=r'Fuel economy (km/L)')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('fuel_economy_usa.json')


# Generate a plot for CO2 emissions of all US light-duty vehicles
data = pd.read_csv('../processed/tidy_automotive_trends.csv')
data = data[(data['Reported quantity']=='Real-world CO2 emissions (g/mi)') & (data['Regulatory Class']=='All')]
agg_data = pd.DataFrame()
agg_data['Year'] = data['Model Year']
agg_data['CO2 emissions'] = round(data['Reported value'] * 0.621371 / 1000.0, 3)

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='Year', type='quantitative', title='Year'),
            y=alt.Y(field=r'CO2 emissions', type='quantitative', title=r'CO2 emissions (kg/km)',
                scale=alt.Scale(domain=[0.2, 0.5])),
            tooltip=[alt.Tooltip(field='Year', type='quantitative', title='Year'),
                     alt.Tooltip(field=r'CO2 emissions', type='quantitative', title=r'CO2 emissions (kg/km)')]
            ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('co2_emissions_usa.json')