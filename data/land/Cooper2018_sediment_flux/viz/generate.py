#%%
import pandas as pd 
import anthro.io
import altair as alt 

# Load the data for sediment masses
data = pd.read_csv('../processed/Cooper2018_table1_sediment_mass.csv')
data['year'] = pd.to_datetime(data['year'], format="%Y")

# Add a descriptive field for interactivity
data['mass_fmt'] = anthro.io.numeric_formatter(data['value'].values * 1E9, sci=True, unit='t')

# Generate visualizations of sediment mass as a function of time
for g, d in data.groupby(['quantity']):
    if g == 'total ':
        g = 'non-agricultural sediment'
    chart = alt.Chart(d).encode(
            x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
            y=alt.Y(field='value', type='quantitative', title=f'{g} mass [Gt]'),
            tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                    alt.Tooltip(field='mass_fmt', type='nominal', title='sediment mass')]
            ).properties(width='container', height=300)
    l = chart.mark_line(color='dodgerblue')
    p = chart.mark_point(color='dodgerblue', filled=True)
    layer = alt.layer(l, p)
    layer.save(f"./{'_'.join(g.split(' ')).replace('/', '_or_')}.json")

#%%
# Plot the total sediment flux as reported in values of cubic kilometers
flux = pd.read_csv('../processed/Cooper2018_table1_sediment_flux.csv')
flux['year'] = pd.to_datetime(flux['year'], format='%Y')
chart = alt.Chart(flux).encode(
        x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
        y=alt.Y(field='flux_km3', type='quantitative', title='sediment volume [km³]'),
        tooltip=[alt.Tooltip(field='year', type='temporal', format='%Y', title='year'),
                alt.Tooltip(field='flux_km3', type='quantitative', format='0.0f', title='volume [km³]')]
        ).properties(width='container', height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('sediment_volume.json')
# %%
# Plot the coal stripping ratio
strip = pd.read_csv('../processed/Cooper2018_coal_stripping_ratio.csv')
strip['year'] = pd.to_datetime(strip['year'], format='%Y')

chart = alt.Chart(strip).encode(
        x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
        y=alt.Y(field='stripping_ratio', type='quantitative', title='tonne of overburden moved per tonne of coal'),
        tooltip=[alt.Tooltip(field='year', type='temporal', format="%Y"),
                 alt.Tooltip(field='stripping_ratio', type='quantitative', format='0.1f',
                            title='stripping ratio')]
        ).properties(width='container', height=300)
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(color='dodgerblue', filled=True)
layer = alt.layer(l, p)
layer.save('coal_stripping_ratio.json')


# %%
