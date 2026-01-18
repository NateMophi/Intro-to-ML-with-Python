import numpy as np
from math import pi

a = np.array([[1,2,4]])
b= np.array([3,5,7])

# print(b.size)
# print(b.ndim)
# print(b.shape)
# print("\n")
# print(a.size)
# print(a.ndim)
# print(a.shape)

x = np.ones((2,3,4), dtype=np.int16)
print (x.shape)
print(x.ndim)
print(x.size)

y = np.arange(1,5.5,0.5).reshape(1,3,3)
print(y)

w = np.linspace(0, pi, 3) ## linspace creates evenly spaced values
print(f"This is w: {w}")
z = np.exp(w * 1j)
print(z)


# N = np.arange(3)
# print(np.exp(N))
# Q= np.arange(10)**3
# Q[:6:3]=100 #from starting index to 5th element, assign every 3rd element to 100
# print(Q)

def f(s, t):
    return 10*s + t
R = np.fromfunction(f, (4,5), dtype=int)
print(R)
print(R[1:3, :])
print("\n")
print(R[1:3, 1])
print("\n")
print(R[:, 2])
print(R[:,3])