import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    for i in range(0, len(x)):
        if x[i] <= 0:
            x[i] = alpha * (math.exp(x[i]) - 1)

    return x