import pandas as pd
import glob

YEAR = 2017
for file in glob.glob('processed/*.csv'):
	name = file.split('/')[1].split('.')[0]
	print(name + '_' + str(YEAR))
	dat = pd.read_csv(file)
	print(dat[dat['year'] == YEAR].reset_index(drop=True))
	print()