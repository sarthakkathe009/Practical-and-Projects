import pandas as pd
import numpy as np

# df.Age and df["Age"] are equivalent ways to access the 'Age' column in the DataFrame

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [23,35, 45, 28],
    "Score": [85, 90, np.nan, 92]
})

print("Original DataFrame:")
print(df)
print("\nFirst 2 rows:")
print(df.head(2))  # Display the first 2 rows of the DataFrame
print("\nShape of the DataFrame:")
print(df.shape)  # Display the shape of the DataFrame
print("\nSummary statistics:")
print(df.describe())  # Display summary statistics of the DataFrame
print("\nInformation about the DataFrame:")
print(df.info())  # Display information about the DataFrame

df["Passed"] = df["Score"] >= 60  # Create a new column 'Passed' based on the 'Score' column
print("\nDataFrame after adding 'Passed' column:\n", df)

df.insert(2,"Country",["USA","Canada","UK","Australia"])  # Insert a new column 'Country' at index 2
print("\nDataFrame after inserting 'Country' column:\n", df)

df.at[2,"Score"] = 88  # Update the 'Score' for Charlie
print("\nDataFrame after updating Charlie's score:\n", df)

df.rename(columns={"Score":"Marks"},inplace=True)
print("\nDataFrame after renaming 'Score' to 'Marks':\n", df)

df.drop(columns=["Country"],inplace=True)  # Drop the 'Country' column
print("\nDataFrame after dropping 'Country' column:\n", df)

sorted_df = df.sort_values(["Marks","Age"],ascending=[False,True])
sorted_df["Rank"] = sorted_df.Marks.rank(ascending=False,method="dense").astype(int)
print("\nSorted Dataframe:\n",sorted_df)

df2 = pd.DataFrame({
    "Name":["Eva","Frank"],
    "Age":[31,26],
    "Score":[88,95]
})

result = pd.concat([df,df2], ignore_index=True)
print("\nAfter concat\n",result)

df_department = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Department": ["IT", "HR", "Finance", "IT"]
})

result_merge = pd.merge(df,df_department,on="Name")
print("\nAfter Merge\n",result_merge)