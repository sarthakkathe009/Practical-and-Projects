import pandas as pd
import numpy as np

arr = np.random.randint(1,10,size=(3,2))
df = pd.DataFrame(arr,columns=["A","B"],index=["r1","r2","r3"])
print("Numpy Array:\n",arr)
print("DataFrame with Lables:\n",df)


df1 = pd.DataFrame({"Name":["Ana","Bob"],"Score":[88,92]})
df2 = pd.DataFrame([{"x":1,"y":2},{"x":3,"y":4}])

arr1 = np.arange(9).reshape(3,3)
df3 = pd.DataFrame(arr1,columns=list("ABC"))

print("DataFrame from Dictionary:\n",df1)
print("DataFrame from List of Dictionaries:\n",df2)
print("DataFrame from Numpy Array:\n",df3)

s = pd.Series([10,20,30],index=["a","b","c"])
df4 = pd.DataFrame(s,columns=["Col1"])

s1 = pd.Series([40,50,60],index=["a","b","c"])
df4.insert(1,"Col2",s1)

df4 = pd.concat([df4,pd.DataFrame([{"Col1":700,"Col2":800},{"Col1":900,"Col2":1000}])],ignore_index=True)

print("DataFrame from Series:\n",df4)