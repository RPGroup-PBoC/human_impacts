from bokeh.models import * 
import numpy as np

def load_js(fname, args):
    """
    Given external javascript file names and arguments, load a bokeh CustomJS
    object
    
    Parameters
    ----------
    fname: str or list of str
        The file name of the external javascript file. If the desired javascript
        exists in multiple external files, they can be provided as a list of
        strings.
    args: dict
        The arguments to supply to the custom JS callback. 
    
    Returns
    -------
    cb : bokeh CustomJS model object
        Returns a bokeh CustomJS model object with the supplied code and
        arguments. This can be directly assigned as callback functions.
    """
    if type(fname) == str:
        with open(fname) as f:
            js = f.read() 
    elif type(fname) == list:
    
        js = ''
        for _fname in fname:
            with open(_fname) as f:
                js += f.read()

    cb = CustomJS(code=js, args=args)
    return cb


def numeric_formatter(values, digits=3, sci=False, unit=''):
    """
    Formats numbers to human-readable formats using single-letter abbreviations
    for orders of magntiude. 

    Parameters
    ----------
    values : list or nd-array of numeric values
        Value which you wish for format in a readable manner
    digits : int
        Number of significant figures to report
    

    Returns
    -------
    str_vals : list 
        List of formatted numbers of the same length as values.
    """
    base_powers = np.floor(np.log10(values))
    str_vals = []
    base_dict = {'p':[-15, -12], 'n':[-12, -9], 'µ':[-9, -6], 'm':[-6, -3],
                 '':[-3, 3], 'K':[3,6], 'M':[6, 9], 'B':[9, 12],
                 'T':[12,15]}
    for i, v in enumerate(values):
        base = base_powers[i]
        for _v, _k in base_dict.items():
            if (base >=_k[0]) & (base < _k[1]):
                n = _k[0]
                l = _v
        val = str(np.round(v*10**-n, decimals=2)) 
        if len(val) <= digits:
            val = val
        else:
            if val[digits-1] == '.':
                end = digits + 1
            else:
                end = digits  
            val = val[:end]
        if (sci == True) & (l == 'B'):
            l = 'G'
        str_vals.append(f'{val}{l}{unit}')
    return str_vals 
