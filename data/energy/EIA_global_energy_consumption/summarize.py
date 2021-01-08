import pandas as pd
import glob

YEAR = 1990
regional_population_data = pd.read_csv('processed/EIA_Population.csv')
recorded_pop = regional_population_data[regional_population_data['year']==YEAR]['population'].sum()
total_population_data = pd.read_csv('processed/EIA_Population_totals.csv')
total_pop = (total_population_data[total_population_data['year']==YEAR]['population']).item()
for file in glob.glob('processed/*.csv'):
	name = file.split('/')[1].split('.')[0]
	print(name + '_' + str(YEAR))
	dat = pd.read_csv(file)
	dat = dat[dat['year'] == YEAR].reset_index(drop=True)

	if 'Per Capita' in dat.columns:
		valname = dat.columns[2]
		total_dat = pd.read_csv('processed/' + name + '_totals.csv')
		total_val = total_dat[total_dat['year'] == YEAR][valname].item()
		recorded_val = dat[valname].sum().item()
		recorded_percent = 100*recorded_val/total_val
		dat = dat.append({'Country Group': 'Miscellaneous', 'year': YEAR, valname: total_val-recorded_val, 'Percentage': 100-recorded_percent, 'Per Capita': (total_val-recorded_val)/(total_pop-recorded_pop)}, ignore_index=True)
		dat = dat.append({'Country Group': 'Total', 'year': YEAR, valname: total_val, 'Percentage': 100, 'Per Capita': total_val/total_pop}, ignore_index=True)
	print(dat)
	print()