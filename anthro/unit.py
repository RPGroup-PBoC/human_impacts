# -*- coding: utf-8 -*-
"""
scale.py
--------------------------
This module contains a set of classes useful in exchanging between scales. 
"""
import numpy as np
import pandas as pd

def _prefixes():
    """
    Defines prefixes for powers of ten. This function is not meant to be
    called directly.
    """
    return {
                    'Y': {'longform':'yotta', 'dimension':24},
                    'Z': {'longform': 'zetta', 'dimension':21},
                    'E': {'longform': 'exa', 'dimension':18},
                    'P': {'longform': 'peta', 'dimension':15},
                    'T': {'longform': 'tera', 'dimension':12},
                    'G': {'longform': 'giga', 'dimension':9},
                    'M': {'longform': 'mega', 'dimension':6},
                    'k': {'longform': 'kilo', 'dimension':3},
                    'h': {'longform': 'hecto', 'dimension':2},
                    'd': {'longform': 'deci', 'dimension':-1},
                    'c': {'longform': 'centi', 'dimension':-2},
                    'm': {'longform': 'milli', 'dimension':-3},
                    'u': {'longform': 'micro', 'dimension':-6},
                    'µ': {'longform': 'micro', 'dimension':-6},
                    'n': {'longform': 'nano', 'dimension':-9},
                    'p': {'longform': 'pico', 'dimension':-12},
                    'f': {'longform': 'femto', 'dimension':-15},
                    'a': {'longform': 'atto', 'dimension':-19},
                    'z': {'longform': 'zepto', 'dimension': -21},
                    'y': {'longform': 'yotto', 'dimension': -24}
            }

def quantity_dimensions(dim_dict):
    """
    Given a dimensional represention, return the corresponding physical 
    quantity. 

    Parameters
    ----------
    dim_dict : dict
        A dictionary holding the dimensional representation of the quantity of
        interest. For each dimension, the exponent must be provided. For
        example, an acceleration of LT^-2 should be described by a dictionary of
        the form
            dim_dict = {'L':1, 'T':-2}
        where the key is the dimension and the value is rational exponent.
    
    Returns 
    --------
    quantity : str
        Returns a string identifying the quantity.

    Raises
    ------
    TypeError:
        A TypeError is returned if the key is not a string and the exponent is
        an integer.
    ValueError:
        A ValueError is returned if the dimension is not one of the following:
            M : Mass
            L : Length
            T : Time
            t/Θ/θ : Temperature
            Q  : Charge
    RuntimeError:
        Returned if provided dimensional representation is not recognized as 
        a physical quantity. 
    """
    for k, v in dim_dict.items():
        if type(k) != str:
            raise TypeError(f'Dimension must be given as str. {type(k)} was provided.')
        if k not in ['L', 'T', 'M', 'Th', 'Θ', 'θ', 'Q']:
            raise ValueError(f'Dimension {k} not a recognized dimension.')
        if type(v) != int:
            raise TypeError(f'Exponent must be a rational number. {type(v)} was provided.')
    
    # Define the physical quantities
    quantities = {'L1T-2'    : 'acceleration',
                  'T-1'     : 'frequency',
                  'L2'      : 'area',
                  'L4'      : 'area moment of inertia',
                  'M1L3T-2'  : 'bending modulus',
                  'M1L2T-2t-1' :  'Boltzmann constant',
                  'Q1'        : 'charge',
                  'M1L2T-2'    : 'chemical potential',
                  'T-1Q1'   : 'electric current',
                  'M1L-3'   : 'density',
                  'L2T-1' : 'diffusivity',
                  'M1L-1T-2': 'elastic modulus',
                  'M1L1T-2Q-1' : 'electric field',
                  'M1L2T-2' : 'energy/free energy/potential/work',
                  'M1L2T-2t-1': 'entropy',
                  'M1L1T-2' : 'force',
                  'LT-2' : 'gravitational constant',
                  'L2T-1' : 'kinematic viscoscity',
                  'L1' : 'length',
                  'L2T-1Q1' : 'magnetic dipole moment',
                  'M1T-1Q-1' : 'magnetic field',
                  'M1' : 'mass',
                  'M1L2': 'moment of inertia',
                  'M1L2T-1': 'angular momentum',
                  'M1L1T-1' : 'linear momentum',
                  'M1L2T-3' : 'power',
                  'M1L-1T-2' : 'pressure/stress',
                  'M1T-2' : 'surface tension',
                  't': 'temperature',
                  'M1T-2': 'tension',
                  'T': 'time',
                  'M1L2T-2': 'torque',
                  'L1T-1': 'velocity',
                  'M1L-1T-1': 'viscosity',
                  'L3': 'volume',
                  'L-3': 'concentration'}

    # Assemble the quantity string
    quant = ''
    for dim in ['M', 'L', 'T', 't', 'Θ', 'θ', 'Q']:
        try: 
            quant += f"{dim}{dim_dict[dim]}"
        except KeyError:
            continue
    try:
        quantity = quantities[quant]
        return quantity
    except KeyError:
        raise RuntimeError('Dimensions do not match a physical quantity.')


class DimensionalUnit(object):
    R"""
    Base class for a quantity with dimension. 
    """

    def __init__(self, unit=None):
        """
        Parameters
        ----------
        unit : str of unit
            The unit of the value as string. This can be a "complicated"
            representation such as `kg*m^2*s` or a more simplistic representation 
            for single units such as `mm` or `ha`. If provided in the formula
            representation, you must not use / for division. Provide `^-1`. 

        """
        # Assign the provided quantities to the object
        self.provided_unit = unit

        # Load the prefixes and units
        self.prefixes = _prefixes() 
        self.length_units = self._units_length()
        self.mass_units = self._units_mass()
        self.time_units = self._units_time()
        self.dim = self._compute_dimensionality()
        dim_dict = {}
        for k, v in self.dim.items():
            dim_dict[k] = v['exponent']
        try: 
            self.phys_quant = quantity_dimensions(dim_dict)
        except RuntimeError:
            self.phys_quant = 'other'
        self.summary = {'unit':unit,
                        'dimensional_representation': self.dim,
                        'quantity': self.phys_quant}
    def _compute_dimensionality(self):
        """
        Computes the dimensionality of the supplied unit.
        """
        unit = self.provided_unit
        if '/' in unit:
            raise ValueError('The symbol `/` was provided in the unit. Use negative exponent to signify division.')
        elif '*' in unit:
           unit_split = unit.split('*')
        else:
            unit_split = [unit]

        dims = {}
        for u in unit_split:
            if '^' in u:
                exponent = int(u.split('^')[1])
                unit = u[0] 
                _unit = u.split('^')[0]
            else: 
                unit = u
                _unit = u
                exponent = 1

            if (_unit == 'm'):
                _unit_info = self.length_units[_unit] 
                dims['L'] = {'shortform':_unit,
                             'longform':_unit_info['longform'],
                             'exponent': exponent}
            if (_unit == 'g') | (_unit == 't'):
                _unit_info = self.length_units[_unit]
                dims['M'] = {'shortform':_unit,
                             'longform': _unit_info['longform'],
                             'exponent': exponent}
            if (_unit == 's') | (_unit == 'yr'):
                _unit_info = self.time_units[_unit]
                dims['T'] = {'shortform':_unit,
                             'longform':_unit_info['longform'],
                             'exponent': exponent}
        self.dims = dims
        return dims

    def _assign_designation(self):            
        """
        Given a dimensional representation, return a dictionary identifying the
        dimensionful group.
        """
        dims = self.dims

    def _assign_prefixes(self, dim, std):
        powers = {std['shortform'] : {'longform':std['longform'],
                                     'dim_to_ref': 0,
                                     'reference':std['longform']}}
        for k,  v in self.prefixes.items():
            powers[f"{k}{std['shortform']}"] = {
                                'longform': f"{v['longform']}{std['longform']}", 
                                'dim_to_ref':dim + v['dimension'],
                                'reference':std['longform']} 

        return powers

    def _units_length(self):
        """
        Returns a dictionary of length unit shorthands and their pertinent 
        dimensionalities relative to the standard unit of meter (m). 
        """
        dim = 0
        lengths = self._assign_prefixes(dim, std={'shortform':'m', 'longform':'meter'})
        return lengths

    def _units_mass(self):
        """
        Returns a dictionary of mass units shorthands and their pertinent 
        dimensionalities relative to the standard unit of grams and tonnes. 
        """
        dim = 0
        g_masses = self._assign_prefixes(dim, std={'shortform':'g', 'longform':'gram'})
        t_masses = self._assign_prefixes(dim, std={'shortform':'t', 'longform':'tonne'})
        masses = {}
        masses.update(g_masses)
        masses.update(t_masses)
        self.mass_units = masses
        return masses

    def _units_time(self):
        """
        Returns a dictionary of tie units shorthands and their pertinent 
        dimensionalities relative to the standard units of seconds (s) and years
        (yr). 
        """
        dim = 0
        s_times = self._assign_prefixes(dim, std={'shortform':'s', 'longform':'seconds'})
        yr_times = self._assign_prefixes(dim, std={'shortform':'yr', 'longform':'year'})
        times = {}
        times.update(s_times)
        times.update(yr_times)
        self.time_units = times 
        return times




