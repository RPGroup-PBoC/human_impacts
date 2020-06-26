# -*- coding: utf-8 -*-
#%%
import imp
import anthro.unit
import pytest
imp.reload(anthro.unit)
acc = anthro.unit.DimensionalUnit('m*s^-2')
acc.summary

# %%
