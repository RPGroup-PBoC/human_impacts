import pandas as pd

population = pd.read_csv('processed/EIA_population.csv')

nat_gas = pd.read_csv('processed/EIA_NatGasConsumption.csv').rename(columns={'Watts': 'NatGas_Watts'})
oil = pd.read_csv('processed/EIA_OilConsumption.csv').rename(columns={'Watts': 'Oil_Watts'})
coal = pd.read_csv('processed/EIA_CoalConsumption.csv').rename(columns={'Watts': 'Coal_Watts'})

total_fossils = nat_gas
total_fossils = pd.merge(total_fossils, oil[['year', 'Country Group', 'Oil_Watts']], on=['year', 'Country Group'], how='outer')
total_fossils = pd.merge(total_fossils, coal[['year', 'Country Group', 'Coal_Watts']], on=['year', 'Country Group'], how='outer')

total_fossils['Watts'] = total_fossils['NatGas_Watts'] + total_fossils['Oil_Watts'] + total_fossils['Coal_Watts']
total_fossils.drop(columns=['NatGas_Watts', 'Oil_Watts', 'Coal_Watts'], inplace=True)
totals = total_fossils[['year', 'Watts']].groupby('year').sum().reset_index().rename(columns={'Watts':'Total'})
total_fossils = pd.merge(total_fossils, totals[['year', 'Total']], on='year', how='outer')
total_fossils['Percentage'] = 100*total_fossils['Watts']/total_fossils['Total']
total_fossils.drop(['Total', 'Per Capita'], axis=1, inplace=True)

total_fossils = pd.merge(total_fossils, population[['year', 'Country Group', 'population']], on=['year', 'Country Group'], how='inner')
total_fossils['Per Capita'] = total_fossils['Watts']/total_fossils['population']
total_fossils.drop(['population'], axis=1, inplace=True)
total_fossils = total_fossils[total_fossils['year'] <= 2017]

total_fossils = total_fossils[['Country Group', 'year', 'Watts', 'Percentage', 'Per Capita']]

total_fossils.to_csv('processed/EIA_FossilFuelConsumption.csv', index=False)

nat_gas_total = pd.read_csv('processed/EIA_NatGasConsumption_totals.csv')
oil_total = pd.read_csv('processed/EIA_OilConsumption_totals.csv')
coal_total = pd.read_csv('processed/EIA_CoalConsumption_totals.csv')
coal_total['Watts'] = nat_gas_total['Watts'] + oil_total['Watts'] + coal_total['Watts']
coal_total.to_csv('processed/EIA_FossilFuelConsumption_totals.csv', index=False)
print(coal_total)