#%%
import numpy as np 
import pandas as pd 
import altair as alt 


# Load the production data. 
data = pd.read_csv('./processed/whale_catches.csv')
data['Year'] = pd.to_datetime(data['Year'], format='%Y')

# Generate JSON vis for subcategories
# for g, d in data.groupby('subcategory'):
chart= alt.Chart(data).encode(
						x=alt.X(field="Year", type="temporal", timeUnit='year',
								title="year"),
						y=alt.Y(field="Catches", 
								type="quantitative",
								title="commercial whale catches"),
					   tooltip=[alt.Tooltip("year:T", timeUnit="year", title="year"),
								alt.Tooltip("catches:Q", format="0.0f", title="total catches")]
					  ).properties(width="container", 
									height=300
					  ).mark_line(color='dodgerblue')
l = chart.mark_line(color='dodgerblue')
p = chart.mark_point(filled=True, color='dodgerblue')
figure = alt.layer(l, p)
figure.save('./viz/whale_catches.json')