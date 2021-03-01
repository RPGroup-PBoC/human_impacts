#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate plots for air pollutant emissions from EDGARv5.0 data
sources = ['PM2.5', 'PM10', 'NMVOC', 'BC', 'SO2', 'NOx']
# Read uncertainties from Crippa et al. (2018)
unc_data = pd.read_csv('../processed/uncertainty_emissions_crippa2018.csv')

for source_ in sources:
    data = pd.read_csv('../processed/'+str(source_)+'_emissions_processed.csv')
    data['year'] = pd.to_datetime(data['Year'].astype(str), format='%Y', errors='coerce')
    agg_data = pd.DataFrame()
    agg_data['year'] = (data[data['World Region']=='World'])['year']
    agg_data['emissions'] = np.round( (data[data['World Region']=='World'])['Emissions (Gg)']/1000.0, 1)
    # Construct uncertainty from fractional uncertainty based on Crippa et al (2018), EDGARv4.3.2
    # Since the emissions distribution is lognormal, the uncertainty bands are
    # given by [base/(1+sigma), base*(1+sigma)].
    agg_data['relative std'] = ((unc_data[unc_data['Pollutant'].str.contains(source_)])['Fractional uncertainty, 1 std']
            ).to_numpy()
    agg_data['lower bound'] = np.divide( agg_data['emissions'], 1 + agg_data['relative std'] )
    agg_data['upper bound'] = np.multiply( agg_data['emissions'], 1 + agg_data['relative std'] )

    chart = alt.Chart(agg_data).encode(
                x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
                y=alt.Y(field=r'emissions', type='quantitative', title=source_+' emissions (Tg)'),
                tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='%Y'),
                         alt.Tooltip(field=r'emissions', type='nominal', title=source_+' emissions (Tg)')]
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
    layer.save(source_+'_emissions.json')

