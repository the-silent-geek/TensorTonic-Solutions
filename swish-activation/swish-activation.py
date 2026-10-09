import numpy as np

def swish(x):
    x = np.asarray(x, dtype=float)
    sigmoid = np.exp(-np.logaddexp(0.0, -x))
    return x * sigmoid
