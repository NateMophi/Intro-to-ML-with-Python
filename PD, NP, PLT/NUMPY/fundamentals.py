import numpy as np

# a = [1,2,3,4,5]
# print(a)
# print(a[1])
# print(a[1:4])

##1D NP ARRAY
# b = np.array([1,2,3,4,5])
# print(b)
# print(b[0])
# print(b[1])
# print(b[3])
# print(type(b))

##MULTI D NP ARRAY
# a_mul = np.array([[3,4,5], [6,8,10], [5,12,13]])
# print(a_mul[0]) #1st list
# print(a_mul[0,1])   #2nd element in 1st list
# print(a_mul[0,2])   #3rd element in 1st list 
# print(a_mul[1,0])   #1st element in 2nd list
# print(a_mul[1,2])
# print(a_mul[2,0])
# print(a_mul[2,1])
# print(a_mul.shape)

# b_mul = np.array([[[4,1,9],[4,2,0],[6,6,6]], [[1,0,1],[6,7,9],[9,1,8]]]) ## 2 lists consisiting of 3 lists w/ 3 elements
# print(b_mul.ndim)
# print(b_mul.size)
# print(b_mul.dtype)
# print(b_mul.shape)

# d= {"Greeting":"hello"}
# c= np.array([[1,2,3],[4,d,8],[7,8,9]])
# print(c.dtype)
# print(c.ndim)
# print(c[0,0])
# print(c[1,1])
# print(type(c[0,0]))

# y = np.full((2,3,4),9)
# print(y)

# z= np.zeros((1,5,2))
# print(z)

# r = np.ones((5,5,3))
# print(r)

# e = np.empty((3,3,3))
# print(e)

##ploting x-values
# xi = np.arange(0,1000,5)
# print(xi)
# xj = np.arange(3,999,7)
# print(xj)
# yi = np.linspace(0,1000,5)
# print(yi)
# yj= np.linspace(3,999,7)
# print(yj)


##NaN and Inf
# print(np.nan)
# print(np.inf)

# print(np.isnan(np.nan))
# print(np.isinf(np.inf))


## math ops w/ numpy
# l1 = [1,2,3,4,5]
# l2 = [6,7,8,9,0]
# a1=np.array(l1)
# a2=np.array(l2)

# print(l1*5)
# print(a1*5)
# ##print(l1 + 5) #impossible to concatenate list w/an int
# print(l1+l2)
# print(a1+a2)
# print(a1-a2)
# print(a1/a2)

# c1 = np.array([1,2,3])
# c2 = np .array([[1],[2]])
# sum = c1+c2
# difference_ = c2-c1
# quotient = c1/c2
# product = c1*c2
# print(sum,"\n", difference_,"\n", quotient,"\n", product,"\n",)

# f = np.array([1,3,4])
# f=np.append(f,[6,8,"hi bro"])
# f = np.insert(f,4,[16,144])
# print(f)

# g= np.array([[1,2,3],[4,5,6]])
# print(np.delete(g,1,0)) # gets rid of second row
# print(np.delete(g,1,1)) # gets rid of second column

#t = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
# print(np.split(t, 5, axis=1))
# print(t.min())
# print(t.max())
# print(t.mean())
# print(t.std())
# print(np.median(t))

# print(t.shape)
# print(t.reshape(5,4))
# print(t.reshape(2,2,5)) #2collections, 2lists, 5elements each
# print(t.reshape(5,2,2)) #5collections, 2lists, 2elements each
# print(t.T)
# print(t.swapaxes(0,1))

# h = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# i = np.array([[11,12,13,14,15],[16,17,18,19,20]])
# hi = np.concatenate((h,i),axis=0) #axis=0 for rows; axis=1 for columns
# print(hi)
# ih = np.concatenate((h,i),axis=1) #axis=0 for rows; axis=1 for columns
# # print(ih)
# print(np.stack((h,i)))
# print(np.vstack((h,i)))
# print(np.hstack((h,i)))


# numbers = np.random.randint(7,77, size=(3,5,2))
# print(numbers)

# np.savetxt("largeArray.csv", t, delimiter=",")
# t = np.load("largeArray.npy")
t = np.loadtxt("largeArray.csv", delimiter=",")
print(t)