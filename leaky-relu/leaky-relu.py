import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    for i in range(0,len(x)):
        if x[i]<0:
            x[i] = alpha*x[i]

    ans = np.asarray(x, dtype=float)
    return ans