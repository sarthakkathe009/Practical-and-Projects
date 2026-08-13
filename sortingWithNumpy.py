import numpy as np
import time

np.random.seed(42)
a = np.random.randint(0,20,10)
print("Original Array:",a)

print("After np.sort():",np.sort(a)) #creates a new sorted array, does not change the original array
print("After edit a is:",a)

a.sort() # in place sorting, changes the original array
print("After a.sort():",a)

b = np.random.randint(0,30,8)
print("Original Array:",b)
print("Desending Sort:",np.sort(b)[::-1])
print("Alternate     :",-np.sort(-b))

scores = np.array([88,92,79,93,95])
order = np.argsort(scores)
print("scores:",scores)
print("Order:",order)
print("sorted:",scores[order])

desc = np.argsort(-scores)
print("descending:",scores[desc])

c = np.array([5,2,3,2,5,2])

print("quicksort(by default):",np.sort(c,kind='quicksort'))
print("mergesort:",np.sort(c,kind='mergesort'))
print("heapsort:",np.sort(c,kind='heapsort'))

c2 = np.random.randint(0, 100000, size=1_000_000)

for kind in ['quicksort', 'mergesort', 'heapsort']:
    
    start = time.perf_counter()
    
    result = np.sort(c2, kind=kind)
    
    end = time.perf_counter()
    
    print(f"{kind}: {end - start:.2f} seconds")

print("#==============Sorting with 2D Array===============#")
np.random.seed(7)
M = np.random.randint(0,100,(4,5))
print("M:\n",M)

row_wise_sort = np.sort(M,axis=1)
print("Row-wise Sort:\n",row_wise_sort)

column_wise_sort = np.sort(M,axis=0)
print("Column-wise Sort:\n",column_wise_sort)

flat = np.sort(M,axis=None)
print("Flatten sorted array:",flat)
print("Flatten sorted array shape:",flat.shape)
print("Flatten sorted array first 10 elements:",flat[:10])

print("M =\n",M)
order = np.argsort(M[:,0])
M_sorted_rows = M[order]

print("Order of first row:",order)
print("Sorted M by row =\n",M_sorted_rows)

N = M.copy()
N.sort(axis=0)
print("N sorted by column(in place) =\n",N)