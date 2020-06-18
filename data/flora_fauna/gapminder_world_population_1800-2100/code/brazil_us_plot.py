"""
This script uses the Altair plotting library to generate a plot of the
populations of Brazil and the US over the range of year from present in 
the original dataset. 
"""
#%%
import pandas as pd
import altair as alt

# Load in the data. 
data = pd.read_csv('../gapminder_world_population_1800-2100_tidy.csv')
data['year_from_present'] = data['year'].values - 2020

# Restrict to only Brazil and the US
restricted = data[data['country'].isin(['Brazil', 'United States'])]

# Generate the plot. 
plot = alt.Chart(restricted).mark_line().encode(
        x=alt.X('year_from_present:Q', axis={'title':'years from present (2020)'}),
        y=alt.Y('population:Q', scale={'type':'log'}),
        color='country:N'
)
plot.save('../media/brazil_us_population.png')
# %%
