import pandas as pd
import glob

# Define groupings (i.e. renewables, fossil fuels, etc).
renewables = ['WindGeneration', 'HydroGeneration', 'SolarGeneration','']


YEAR = 2017
for file in glob.glob('processed/*.csv'):
	name = file.split('/')[1].split('.')[0]
	print(name + '_' + str(YEAR))
	dat = pd.read_csv(file)
	dat = dat[dat['year'] == YEAR].reset_index(drop=True)

	if 'Per Capita' in dat.columns:
		valname = dat.columns[2]
		total_val = dat[valname].sum()
		total_pop = (dat[valname]/dat['Per Capita']).sum()
		dat = dat.append({'Country Group': 'Total', 'year': YEAR, valname: total_val, 'Percentage': 100.0, 'Per Capita': total_val/total_pop}, ignore_index=True)
	print(dat)
	print()