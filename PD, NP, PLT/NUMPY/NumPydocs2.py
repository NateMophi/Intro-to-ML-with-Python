import numpy as np
from numpy import pi
import numpy.random as rg

# Changing an array's shape
a = np.floor(10 * rg.random((3,4)))
# ABOVE var created is 3X4 a matrix w/ randomly
# generated numbers from 0-1, multiplies these numbers by 10 and round em
# to the nearest integer
# print(a, "\n")
# print(a.ravel())
# a.resize((2,6))
# print(a)
# print("\n")
# print("\n")
# print(a.reshape(3,-1)) 

# ARRAY stacking
b = np.floor(10 * rg.random((2,2)))
c = np.floor(10 * rg.random((2,2)))

# print(b)
# print("\n")
# print(c)
# print("\n")
# print(np.vstack((b,c)))
# print(np.hstack((b,c)))
# print("\n")
# print(np.stack((b,c)))

# Copy and Views
d = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
e = d
# print(e is d)
# f = d.view()
# print(f.base is d)
# f = f.reshape((2,6)) # d's shaoe doesn't change
# f[0,4] = 679         # d's data achnages
# print(f)
# print(d)

s = d[:, 1:3]
s[:]=10
print(d)
print(s)
print("\n")
h = d.copy()
h[0,0] = 345
print(d)
print(h)