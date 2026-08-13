import numpy as np
print(np.__version__)

data = [1,2,3,4,5]
arr = np.array(data)
print(arr, type(arr), arr.shape, arr.ndim, arr.dtype)
# output: [1 2 3 4 5] <class 'numpy.ndarray'> (5,) 1 int64
#(5,) means 5 rows and 1 dimension, int64 means the data type of the array is integer with 64 bits

data2 = [1,2,3.4,4,5]
arr2 = np.array(data2)
print(arr2, type(arr2), arr2.shape, arr2.ndim, arr2.dtype)
# output: [1.  2.  3.4 4.  5. ] <class 'numpy.ndarray'> (5,) 1 float64

data3 = [1,2,'a',4,5]
arr3 = np.array(data3)
print(arr3, type(arr3), arr3.shape, arr3.ndim, arr3.dtype)
# output: ['1' '2' 'a' '4' '5'] <class 'numpy.ndarray'> (5,) 1 <U21
#<U21 means the data type of the array is unicode string with 21 characters

data4 = [1,2,3,4,5]
arr4 = np.array(data4, dtype='float32') # chnaging the data type of the array to float32
print(arr4, type(arr4), arr4.shape, arr4.ndim, arr4.dtype)

data5 = [[1,2,3],[4,5,6]]
arr5 = np.array(data5)
print(arr5, type(arr5), arr5.shape, arr5.ndim, arr5.dtype)
# (2, 3) means 2 rows and 3 columns, 2 dimensions, int64 means the data type of the array is integer with 64 bits

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix, matrix.shape)

print("----------------------")

zero1 = np.zeros(5) #float64 by default
print(zero1)

print("----------------------")

zeros = np.zeros((2,3))
ones = np.ones((2,3),dtype = int)
full = np.full((2,3),7)
print(zeros,"\n\n",ones,"\n\n",full)

arng = np.arange(0,10)
print(arng)
print()

arng = np.arange(0,10,4) # 4 is the step size
print(arng)
print()

grid = np.arange(1,13).reshape(3,4) # number of elements must be equal to the product of the dimensions (3*4=12)
print(grid)

arr1D = np.array([1,2,3],dtype=np.int16) #by default, numpy uses int64 for integers, but we can change it to int16 using dtype parameter
print('arr1D shape:',arr1D.shape)
print('arr1D ndim:',arr1D.ndim)
print()

A = np.arange(24).reshape(4,6)
print('A',A)
print('A shape:',A.shape)
print('A ndim:',A.ndim)
print('A size(elements):',A.size)
print('A for each element(byte/s):',A.itemsize)
print('A total bytes:',A.nbytes)
print()

B = np.arange(24).reshape(2,3,4)
print('B',B)
print('B shape:',B.shape)
print('B ndim:',B.ndim)
print()