import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    l = 1.0507009873554804934193349852946
    a = 1.6732632423543772848170429916717

    for i in range(0, len(x)):
        if x[i] > 0 :
            x[i] = round(l*x[i], 4)
        else:
            x[i] = round ( l*a*(math.exp(x[i]) - 1), 4)
    return x