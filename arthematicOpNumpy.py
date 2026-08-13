import numpy as np

arr = np.arange(1,6)
print("arr      :",arr)

print("arr + 5  :",arr + 5)
print("arr - 3  :",arr - 3)
print("arr * 5  :",arr * 5)
print("arr // 2 :",arr // 2)
print("arr / 2  :",arr / 2)
print("arr % 2  :",arr % 2)
print("arr ** 2 :",arr ** 2)

arr2 = np.arange(11,16)
print("arr2     :",arr2)
print("np.dot(arr,arr2):",np.dot(arr,arr2))

arr2D = np.array([[1,2,3],[4,5,6]])
print("arr2D    :\n",arr2D)
print("arr2D + 5:\n",arr2D + 5)
print("arr2D - 3:\n",arr2D - 3)
print("arr2D * 5:\n",arr2D * 5)
print("arr2D // 2:\n",arr2D // 2)
print("arr2D / 2:\n",arr2D / 2)

A1 = np.arange(1,10)
B1 = np.arange(11,20)
print("A1       :",A1)
print("B1       :",B1)
print("A1 + B1  :",A1 + B1)
print("A1 - B1  :",A1 - B1)
print("A1 * B1  :",A1 * B1)
print("A1 // B1 :",A1 // B1)

A = np.arange(1,10).reshape(3,3)
B = np.arange(11,20).reshape(3,3)

print("A        :\n",A)
print("B        :\n",B)
print("A + B    :\n",A + B)
print("A - B    :\n",A - B)
print("A * B    :\n",A * B)
print("A // B   :\n",A // B)

C = A + B
print("C        :\n",C)
print("C.sum():",C.sum())
print("C.sum():",C.sum(axis=1)) # sum of each row
print("C.sum():",C.sum(axis=0)) # sum of each column
print("C.mean():",C.mean(axis=0))
print("Standard Deviation of C:",C.std())

A2 = np.arange(1,13).reshape(3,4)
print(A2,"\n")

AT = A2.T
print(AT,"\n")

print("Matrix Multiplication:\n",A2 @ AT)