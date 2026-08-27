import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [23, 35, 45, 28, 31],
    "Score": [88, 92, 79, 95, 85],
},index=["a", "b", "c", "d", "e"])

print(df)
print("\nSelecting single column:\n",df["Age"])
print("\nSelecting multiple column:\n",df[["Age","Score"]])
print("\nPrinting Dataframe:\n",df.Age.head(4))

print("\nUsing loc():\n",df.loc[['a','b'],"Name"])
print("\nUsing iloc():\n",df.iloc[2:5,2])

print("\nWith Condition:\n",df[df.Score>80])
print("\nUsing loc() with Condition:\n",df.loc[df.Age.between(25,40)])

mask = (df.Score > 30) & (df.Age < 35)
print("\ndf[mask]:\n",df[mask])

rows = ["a","b","c"]; cols=["Name", "Score"]
print("\ndf.loc[rows,cols]:\n",df.loc[rows,cols])

boolean_rows = df.Age % 2 ==0
print("\nboolean_rows:\n",boolean_rows)
print("\ndf[boolean_rows]:\n",df[boolean_rows])

df.loc[df.Score < 85,"Grade"] = "B"
print("\nSlicing:\n",df)