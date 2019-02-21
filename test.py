import numpy as np

def fu(x):
    res = np.sin(x)+2*np.sqrt(x)
    return res

print(fu(5))