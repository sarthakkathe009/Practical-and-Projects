import numpy as np

arr = np.arange(10)
print("First element:",arr[0])
print("Last element:",arr[-1])

print("======Slicing=====")

print("arr[3:]",arr[3:])
print("arr[-5:]",arr[-5:])
print("arr[2:8]",arr[2:8])
print("arr[4:10:2]",arr[4:10:2])
print("arr[::2]",arr[::2])
print("arr[::2]",arr[::2])
print("In reverse order(arr[::-1])",arr[::-1])
print("In reverse order skipping specific count(arr[::-3])",*arr[::-3])

sub = arr[2:6] # view of arr from index 2 to 5
print(sub)
sub[:] = -1
print("arr after edit:",arr) #changes to original array

arr2 = np.arange(1,13).reshape(3,4)
print(arr2)

print("Row at index 1",arr2[1,:])
print("Column at index 2",arr2[:,2])
print("Element:",arr2[2,3])

block = arr2[1,:]
print("arr2[1,:]",block);print()

block = arr2[:,1]
print("arr2[:,1]",block);print()

block = arr2[0:2,1:3]
print("arr2[0:2,1:3]\n",block);print()

block = arr2[0:2,]
print("arr2[0:2,]\n",block);print()

block = arr2[:,0:2]
print("arr2[:,0:2]\n",block);print()

block = arr2[0:2,1]
print("arr2[0:2,1]\n",block);print()

block = arr2[0:2,:1]
print("arr2[0:2,1]\n",block);print()

block = arr2[0,1:3]
print("arr2[0,1:3]\n",block);print()

block[:] = 99
print("arr2 after edit:\n",arr2)