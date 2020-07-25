import numpy as np
import pandas as pd 
from tqdm import tqdm

def bootstrap(x, iter=int(1E6), return_samples=False):
    """
    Performs a simple bootstrap resampling method on an array of data. 

    Parameters
    ----------
    x : numpy array
        A one-dimensional numpy array containing values you wish to bootstrap.
        If this array is < 10 values long, a warning will be raised that the 
        sampling distribution is small and the resulting resampled distribution
        may not capture the full data generating distribution
    iter: integer
        Number of iterations to perform. Default is 10^6
    return_samples : bool 
        If true, a pandas DataFrame of the resampled distributions will be
        returned.  

    Returns
    -------
    statistics : dict
        Dictionary of statistics of the resampled distribution. This includes 
        details about the originally supplied data as well as the mean value,
        standard deviation, and confidence intervals.
    """

    
    means = np.empty(iter) 
    dfs = []
    for i in tqdm(range(iter), desc='Performing bootstrap sampling'):
        resamp = np.random.choice(x, size=len(x), replace=True)
        means[i] = resamp.mean()

        if return_samples:
            _df = pd.DataFrame([])
            _df['value'] = resamp
            _df['iter'] = i + 1
            dfs.append(_df)

    # Compute confidence intervals of the means.
    mean_val = means.mean()
    bounds_ci = {'99%': (0.5, 99.5), '95%': (2.5, 97.5), '90%': (5, 95),
           '75%': (12.5, 87.5), '50%': (25, 75), '25%': (37.5, 62.5),
           '10%': (45, 55), '5%': (47.5,  52.5), '1%': (49.5, 50.5)} 
    cis = {} 
    for k, v in bounds_ci.items():
        bounds = np.percentile(means, v)
        cis[k] = bounds

    statistics['original_data'] = x
    statistics['resampled_means'] = means
    statistics['mean_value'] = mean_val
    statistics['confidence_intervals'] = cis

    if return_samples:
        _df = pd.concat(dfs, sort=False)
        return [statistics, _df]
    else:
        return statistics
    