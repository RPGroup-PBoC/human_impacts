#%%
import numpy as np
import pandas as pd 
import altair as alt
import glob

alt.renderers.enable('default')

filenames = glob.glob('../processed/*_totals.csv')
filenames.remove('../processed/EIA_population_totals.csv')
title_dict = {'OilProduction': 'Oil Production',
				'CoalConsumption': 'Coal Consumption',
				'RenewableGeneration': 'Renewable Power Generation',
				'WindGeneration': 'Wind Generation',
				'SolarGeneration': 'Solar Power Generation',
				'HydroGeneration': 'Hydroelectric Power Generation',
				'CoalProduction': 'Coal Production',
				'NatGasProduction': 'Natural Gas Production',
				'NatGasConsumption': 'Natural Gas Consumption',
				'OilConsumption': 'Oil Consumption',
				'TotalConsumption': 'Total Energy Consumption',
				'NuclearGeneration': 'Nuclear Power Generation',
				'FossilFuelConsumption': 'Total Fossil Fuels Consumption'}
units_dict = {'cubic meters': 'km^3', 'Watts': 'TW', 'kg': 'MT'}
units_conversion = {'Watts': 10**(-12), 'cubic meters': 10**(-9), 'kg': 10**(-9)}

for file in filenames:
	data = pd.read_csv(file)
	name = file.split('/')[2].split('.')[0]
	title = title_dict[name.split('_')[1]]
	valname = data.columns[1]
	if valname in units_dict.keys():
		unit_name = units_dict[valname]
	else:
		unit_name = valname
	if valname in units_conversion.keys():
		data[valname] *= units_conversion[valname]
	data['year'] = pd.to_datetime(data['year'], format='%Y')
	data.rename(columns={valname:unit_name}, inplace=True)
	
	chart = alt.Chart(data).encode(
				x=alt.X(field='year', type='temporal', timeUnit='year', title='year'),
				y=alt.Y(field=unit_name,  type='quantitative', title=f'{title} [{unit_name}]'),
				tooltip=[alt.Tooltip(field='year', type='temporal', title='year', format='.2f'),
						alt.Tooltip(field=unit_name, type='nominal')]
				).properties(
					width="container",
					height=300
				)

	l = chart.mark_line(color='dodgerblue')
	p = chart.mark_point(color='dodgerblue', filled=True)
	layer = alt.layer(l, p)
	layer.save(f'./{name}.json')
# %%