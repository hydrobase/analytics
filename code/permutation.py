from __future__ import division

import numpy as np


def _test_statistic(arr, m):
    """Calculate the difference-in-means statistic.
    This is based on an input array, `arr`, where the first `m`
    observations correspond to the treatment group.

    Parameters
    ----------
    arr : np.ndarray
        observed outcomes
    m : int
        number of units in the treatment group

    Returns
    -------
    test_statistic : float

    Examples
    --------
    >>> m = 3
    >>> a = np.ones(m)
    >>> b = np.zeros(m)
    >>> arr = np.append(a, b)
    >>> _test_statistic(arr, m)
    1.0
    """
    return np.mean(arr[:m]) - np.mean(arr[m:])

def pt(arr, m, permutations=10000, two_tailed=True):
    """Estimate the permutation test p-value

    Parameters
    ----------
    arr : np.ndarray
        observed outcomes
    m : int
        number of units in the treatment group
    permutations : int
        number of times to shuffle `arr`
    two_tailed : bool
        whether or not to use a two-tailed hypothesis

    Returns
    -------
    p_value : float
        the proportion of times we observe a value as extreme as the
        experimental estimate of the average treatment effect

    Notes
    -----
    The first `m` observations must correspond to the treatment group

    Examples
    --------
    >>> np.random.seed(42)
    >>> N, m = 50, 25
    >>> t = np.random.normal(loc=10, size=m)
    >>> c = np.random.normal(loc=5, size=N-m)
    >>> arr = np.append(t, c)
    >>> pt(arr, m)
    0.0
    """
    np.random.seed(42)
    arr = arr.copy()
    baseline = _test_statistic(arr, m)
    v = []
    for _ in range(permutations):
        np.random.shuffle(arr)
        v.append(_test_statistic(arr, m))
    if two_tailed:
        baseline = np.abs(baseline)
        v = np.abs(v)
    else:
        v = np.array(v)
    return (v >= baseline).sum() / permutations
