import numpy as np

l = np.arange(0.10000)

f = np.vectorize(lambda x: x**2)
f(l)
