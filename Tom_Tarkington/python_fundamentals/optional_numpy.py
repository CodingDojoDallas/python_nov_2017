import numpy as np

a = np.arange(1,16).reshape(3,5)
print a
print a.shape
print a.ndim
b = np.arange(1,16).reshape(3,5)
c= a*b
print c
d= a+b
print d
d.resize(5,3)
print d
