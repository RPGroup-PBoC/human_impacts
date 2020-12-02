import pandas as pd
import glob

def aggregate_by_region(country_groupings, data, value_str='value'):
	joint = pd.merge(data[['iso', 'year', value_str]], country_groupings[['iso', 'Country Group']], on='iso', how='inner')
	output = joint[['Country Group', 'year', value_str]].groupby(['Country Group', 'year']).sum().reset_index()
	totals = joint[['year', value_str]].groupby('year').sum().reset_index().rename(columns={value_str:'Total'})
	output = pd.merge(output, totals[['year', 'Total']], on='year', how='outer')
	output['Percentage'] = 100*output[value_str]/output['Total']
	output.drop(['Total'], axis=1, inplace=True)
	return output

def load_eia_json(file):
	data = pd.read_json(file)
	data = data.explode('data').reset_index()
	data = pd.concat([data.drop(['data'], axis=1), pd.json_normalize(data['data'])], axis=1)
	data = data[pd.notnull(data['value'])]
	data = data[data['value'].apply(lambda x: isinstance(x, int) or isinstance(x, float))]
	data['date'] = pd.to_datetime(data['date'], unit='ms')
	data['year'] = pd.DatetimeIndex(data['date']).year
	data = data[data['year'] <= 2018]
	return data.reset_index()

def per_capita(region_populations, data, value_str='value'):
	joint = pd.merge(data[['Country Group', 'year', value_str]], region_populations[['Country Group', 'year', 'population']], on=['Country Group', 'year'], how='inner')
	return joint[value_str].divide(joint['population'])

# get FAO country groups
regions = ['Africa', 'Europe', 'Northern America', 'Central America', 'South America', 'Asia', 'Oceania']
country_groupings = pd.read_csv('source/FAOSTAT_groupings.csv')
country_groupings.loc[country_groupings['Country Group'] == 'Caribbean', 'Country Group'] = 'Northern America'
country_groupings = country_groupings[country_groupings['Country Group'].isin(regions)]
country_groupings.rename(columns={'ISO3 Code': 'iso'}, inplace=True)

# get country group populations
country_populations = load_eia_json('source/EIA_population.json')
region_populations = aggregate_by_region(country_groupings, country_populations)
region_populations.rename(columns={'value': 'population'}, inplace=True)
region_populations['population'] *= 1000

unit_conversions = {'TJ': (31688.7646,'Watts'), 'MT': (10**6,'kg'), 'BCM': (10**9,'cubic meters'), 'TBPD': (1000*0.1589872949*365,'cubic meters')}
filenames = glob.glob('source/*.json')
filenames.remove('source/EIA_Population.json')
for file in filenames:
	print(file)
	data = load_eia_json(file)
	conversion = unit_conversions[data['unit'][0]]
	data['value'] *= conversion[0]
	data.rename(columns={'value': conversion[1]}, inplace=True)
	regional_data = aggregate_by_region(country_groupings, data, value_str=conversion[1])
	regional_data['Per Capita'] = per_capita(region_populations, regional_data, value_str=conversion[1])
	name = file.split('/')[1].split('.')[0]
	regional_data.to_csv(f'processed/{name}.csv', index=False)

region_populations.to_csv('processed/EIA_population.csv', index=False)

