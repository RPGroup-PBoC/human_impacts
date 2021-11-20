#%%
import numpy as np 
import pandas as pd 
import altair as alt 
import anthro.io

# Generate plots for greenhouse gas emissions from EDGARv6.0 data
sources = ['CH4', 'N2O']
# Read uncertainties from Janssens-Maenhout et al (2019)
unc_data = pd.read_csv('../processed/uncertainty_emissions_Janssens_Maenhout.csv')

for source_ in sources:
    data = pd.read_csv('../processed/'+str(source_)+'_emissions_processed.csv')
    data['year'] = pd.to_datetime(data['Year'].astype(str), format='%Y', errors='coerce')
    agg_data = pd.DataFrame()
    agg_data['year'] = (data[data['C_group_IM24_sh']=='World'])['year']
    # Convert from Gg to Tg
    agg_data['emissions'] = np.round( (data[data['C_group_IM24_sh']=='World'])['Emissions (Gg)']/1000.0, 1)
    # Construct uncertainty from relative uncertainty based on Janssens-Maenhout et al (2019), EDGARv4.3.2
    # Rthe uncertainty bands are given by [base*(1-2_sigma), base*(1+2_sigma)].
    agg_data['relative std'] = ((unc_data[unc_data['Greenhouse Gas'].str.contains(source_)])['Relative uncertainty, 2 std']
            ).to_numpy()
    agg_data['lower bound'] = np.multiply( agg_data['emissions'], 1 - agg_data['relative std'] )
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

