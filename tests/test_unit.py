# -*- coding: utf-8 -*-
#%%
import imp
import anthro.unit
import pytest
imp.reload(anthro.unit)
acc = anthro.unit.DimensionalUnit('km*yr^-2')
velo = anthro.unit.UnitConversion(value=10, unit='m*s^-1')

acc.summary

# %%
velo.unit

# %%
velo.unit.summary

# %%
