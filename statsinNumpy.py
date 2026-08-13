import numpy as np

np.random.seed(0)  # For reproducibility
x = np.random.randint(1,101,12)
print("x =",x)

print("min(x) =",np.min(x))
print("max(x) =",np.max(x))
print("mean(x) =",np.mean(x))
print("std(x) =",np.std(x))
print("median(x) =",np.median(x))
print("sum(x) =",np.sum(x))
print("var(x) =",np.var(x))
print("cumsum(x) =",np.cumsum(x))
print("cumprod(x) =",np.cumprod(x))

M = np.arange(1,13).reshape(3,4)
print("M =\n",M)

print("min(column wise)",M.min(axis=0))
print("sum(row wise)",M.sum(axis=1))
print("mean(column wise)",M.mean(axis=0))
print("std(row wise)",M.std(axis=1))