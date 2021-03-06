#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Load the production data. 
data = pd.read_csv('../processed/global_carbon_budget_processed.csv')
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# %%
# Generate a plot for net natural sinks
agg_data = pd.DataFrame()
agg_data['year'] = data[(data['Sink/source type']=='natural sink') &
                        (data['Units']=='Pg CO2 yr-1') &
                        (data['Reported value']=='mean')]['Year']
agg_data['net sink'] = data[(data['Sink/source type']=='natural sink') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='mean')]['Value']
agg_data['std'] = (data[(data['Sink/source type']=='natural sink') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='standard deviation')]['Value']).to_numpy()
agg_data['lower bound'] = agg_data['net sink'] - agg_data['std'] # 68% confidence interval
agg_data['upper bound'] = agg_data['net sink'] + agg_data['std'] # 68% confidence interval

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'net sink', type='quantitative', title=r'Net sink (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'net sink', type='nominal', title=r'net sink')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y('lower bound:Q', scale=alt.Scale(zero=False)),
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('natural_CO2_sink.json')


# %%
# Generate a plot for land-use change emissions
agg_data = pd.DataFrame()
agg_data['year'] = data[(data['Sink/source type']=='land-use change emissions') &
                        (data['Units']=='Pg CO2 yr-1') &
                        (data['Reported value']=='mean')]['Year']
agg_data['land-use change emissions'] = data[(data['Sink/source type']=='land-use change emissions') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='mean')]['Value']
agg_data['std'] = (data[(data['Sink/source type']=='land-use change emissions') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='standard deviation')]['Value']).to_numpy()
agg_data['lower bound'] = agg_data['land-use change emissions'] - agg_data['std'] # 68% confidence interval
agg_data['upper bound'] = agg_data['land-use change emissions'] + agg_data['std'] # 68% confidence interval

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'land-use change emissions', type='quantitative', title=r'Land-use change emissions (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'land-use change emissions', type='nominal', title=r'land-use change emissions')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y('lower bound:Q', scale=alt.Scale(zero=False)),
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('land_use_CO2_source.json')

# %%
# Generate a plot for fossil fuel emissions
agg_data = pd.DataFrame()
agg_data['year'] = data[(data['Sink/source type']=='fossil fuel and industry') &
                        (data['Units']=='Pg CO2 yr-1') &
                        (data['Reported value']=='mean')]['Year']
agg_data['fossil fuels'] = data[(data['Sink/source type']=='fossil fuel and industry') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='mean')]['Value']
agg_data['std'] = (data[(data['Sink/source type']=='fossil fuel and industry') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='standard deviation')]['Value']).to_numpy()
agg_data['lower bound'] = agg_data['fossil fuels'] - agg_data['std'] # 68% confidence interval
agg_data['upper bound'] = agg_data['fossil fuels'] + agg_data['std'] # 68% confidence interval

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'fossil fuels', type='quantitative', title=r'Fossil fuel emissions (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'fossil fuels', type='nominal', title=r'fossil fuels')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y('lower bound:Q', scale=alt.Scale(zero=False)),
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('fossil_fuels_CO2_source.json')

# %%
# Generate a plot for atmospheric CO2 growth rate
agg_data = pd.DataFrame()
agg_data['year'] = data[(data['Sink/source type']=='atmospheric growth') &
                        (data['Units']=='Pg CO2 yr-1') &
                        (data['Reported value']=='mean')]['Year']
agg_data['atmospheric growth'] = data[(data['Sink/source type']=='atmospheric growth') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='mean')]['Value']
agg_data['std'] = (data[(data['Sink/source type']=='atmospheric growth') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='standard deviation')]['Value']).to_numpy()
agg_data['lower bound'] = agg_data['atmospheric growth'] - agg_data['std'] # 68% confidence interval
agg_data['upper bound'] = agg_data['atmospheric growth'] + agg_data['std'] # 68% confidence interval

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'atmospheric growth', type='quantitative', title=r'Atmospheric [CO2] growth (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'atmospheric growth', type='nominal', title=r'atmospheric growth')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y('lower bound:Q', scale=alt.Scale(zero=False)),
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('atmos_growth_CO2_source.json')

# %%

# Generate a plot for net oceanic CO2 uptake
agg_data = pd.DataFrame()
agg_data['year'] = data[(data['Sink/source type']=='ocean sink') &
                        (data['Units']=='Pg CO2 yr-1') &
                        (data['Reported value']=='mean')]['Year']
agg_data['ocean sink'] = data[(data['Sink/source type']=='ocean sink') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='mean')]['Value']
agg_data['std'] = (data[(data['Sink/source type']=='ocean sink') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='standard deviation')]['Value']).to_numpy()
agg_data['lower bound'] = agg_data['ocean sink'] - agg_data['std'] # 68% confidence interval
agg_data['upper bound'] = agg_data['ocean sink'] + agg_data['std'] # 68% confidence interval

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'ocean sink', type='quantitative', title=r'Oceanic [CO2] sink (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'ocean sink', type='nominal', title=r'ocean sink')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y('lower bound:Q', scale=alt.Scale(zero=False)),
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('ocean_CO2_sink.json')

# %%

# Generate a plot for net land CO2 uptake
agg_data = pd.DataFrame()
agg_data['year'] = data[(data['Sink/source type']=='land sink') &
                        (data['Units']=='Pg CO2 yr-1') &
                        (data['Reported value']=='mean')]['Year']
agg_data['land sink'] = data[(data['Sink/source type']=='land sink') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='mean')]['Value']
agg_data['std'] = (data[(data['Sink/source type']=='land sink') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='standard deviation')]['Value']).to_numpy()
agg_data['lower bound'] = agg_data['land sink'] - agg_data['std'] # 68% confidence interval
agg_data['upper bound'] = agg_data['land sink'] + agg_data['std'] # 68% confidence interval

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'land sink', type='quantitative', title=r'Land [CO2] sink (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'land sink', type='nominal', title=r'land sink')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y('lower bound:Q', scale=alt.Scale(zero=False)),
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('land_CO2_sink.json')

# %%

# Generate a plot for anthropogenic CO2 emissions
agg_data = pd.DataFrame()
agg_data['year'] = data[(data['Sink/source type']=='anthropogenic emissions') &
                        (data['Units']=='Pg CO2 yr-1') &
                        (data['Reported value']=='mean')]['Year']
agg_data['anthropogenic emissions'] = data[(data['Sink/source type']=='anthropogenic emissions') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='mean')]['Value']
agg_data['std'] = (data[(data['Sink/source type']=='anthropogenic emissions') &
                            (data['Units']=='Pg CO2 yr-1') &
                            (data['Reported value']=='standard deviation')]['Value']).to_numpy()
agg_data['lower bound'] = agg_data['anthropogenic emissions'] - agg_data['std'] # 68% confidence interval
agg_data['upper bound'] = agg_data['anthropogenic emissions'] + agg_data['std'] # 68% confidence interval

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'anthropogenic emissions', type='quantitative', title=r'Anthropogenic [CO2] emissions (Pg CO2 yr-1)'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'anthropogenic emissions', type='nominal', title=r'anthropogenic emissions')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y('lower bound:Q', scale=alt.Scale(zero=False)),
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('anthro_CO2_emissions.json')

# Generate a plot for CO2 flux number: Anthropogenic emissions / natural sinks
data_number = pd.read_csv('../processed/co2_flux_number_dimensioness.csv')
data_number['Year'] = pd.to_datetime(data_number['Year'], format='%Y')
agg_data = pd.DataFrame()
agg_data['year'] = data_number[(data_number['Reported value']=='mean')]['Year']
agg_data['co2 flux number'] = data_number[(data_number['Reported value']=='mean')]['Value']

agg_data['std'] = (data_number[(data_number['Reported value']=='standard deviation')]['Value']).to_numpy()
agg_data['lower bound'] = agg_data['co2 flux number'] - agg_data['std'] # 68% confidence interval
agg_data['upper bound'] = agg_data['co2 flux number'] + agg_data['std'] # 68% confidence interval

chart = alt.Chart(agg_data).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field=r'co2 flux number', type='quantitative', title=r'Anthropogenic emissions / natural sinks'),
            tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                     alt.Tooltip(field=r'co2 flux number', type='nominal', title=r'Anthropogenic emissions / natural sinks')]
            ).properties(width='container', height=300)

# Add uncertainty bands
bands = chart.mark_area(color='dodgerblue', fillOpacity=0.4).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y('lower bound:Q', scale=alt.Scale(zero=False)),
            y2='upper bound:Q'
        ).properties(width='container', height=300)

l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(bands, l, p)
layer.save('CO2_flux_number.json')
