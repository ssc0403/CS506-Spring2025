import numpy as np 
import pandas as pd 


# 1) Data Structures

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 42, 18, 36, 29],
    'Salary': [50000, 60000, 45000, 52000, 58000],
    'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance']
}

# Create and print a DataFrame and call it df with the above data
df = pd.DataFrame(data)
print("DataFrame:\n", df) 


# 2) Reading & Writing Data

# Click the folder icon on the left to observe the current filesystem
# Then, let's save our DataFrame to a CSV
df.to_csv("employee_data.csv", index=False)

# Then read it back into a new DataFrame and print it
df_csv = pd.read_csv("employee_data.csv")
print("DataFrame read from CSV:\n", df_csv.head())


# 3) Inspecting & Exploring

# Print the shape, first few rows, summary, and statistics of the DataFrame
print("Shape of df:", df.shape)
print()
print("First few rows:", df.head())
print()
print("Info:")
df.info()
print()
print("Describe:\n", df.describe())
print()


# 4) Selecting & Filtering

# Print the ages of all the employees in df
ages = df["Age"]
print("Ages:\n", ages)
print()

# Filter and print the employees with a salary greater than 55000 in df
filtered_df = df[df["Salary"] > 55000]
print("Employees with salary > 55000:\n", filtered_df)


# 5) Modifying DataFrames

# Drop the "Department" column from df and print it
df.drop("Department", axis=1, inplace=True)
print("After department column was dropped:\n", df)
print()

# Create and print a new DataFrame without the third employee (row)
df_dropped_3rd_row = df.drop(3) # axis=0 is the default
print(df_dropped_3rd_row)
print()

# Create and print a new DataFrame without the "Charlie" (just think, don't code: how might you do this in place?)
df_dropped_charlie = df[df["Name"] != "Charlie"] # not in place
# df = df[df["Name"] != "Charlie"] # in place
print(df_dropped_charlie)
print()

# Create a new column by increasing the salaries by 10% in df and print it
df["Salary_After_Bonus"] = df["Salary"].apply(lambda x: x * 1.10)
print("Added 10% bonus to Salary:\n", df.head())


# 6) Handling Missing Values

# Example: Let's artificially introduce a missing value
df.loc[2, "Age"] = np.nan
print("DataFrame with a missing value:\n", df)
print()

# Create a new DataFrame by dropping the rows of df with missing data and print it
df_no_na = df.dropna()
print("Dropped missing rows:\n", df_no_na)
print()

# Create a new DataFrame by filling the rows of df with missing data and print it
df_filled = df.fillna(0)
print("Filled missing data with 0:\n", df_filled)


# 7) Merging & Concatentation 

# Let's create a second DataFrame
dept_info = pd.DataFrame({
    'Department': ['HR', 'Finance', 'IT', 'Marketing'],
    'Location': ['Building A', 'Building B', 'Building C', 'Building D']
})
df["Department"] = ["HR", "Finance", "IT", "HR", "Finance"]
print(df)
print()
# Create a new DataFrame by merging dept_info with df on the "Department" column and print it
merged_df = df.merge(dept_info, on="Department", how="left")
print("Merged DataFrame:\n", merged_df)

# Concatenation: add more rows to the existing columns
df_part2 = pd.DataFrame({
    'Name': ['Frank', 'Grace'],
    'Age': [33, 27],
    'Salary': [61000, 49000],
    'Department': ['IT', 'HR'],
    'Salary_After_Bonus': [67100, 53900]
})

# Create a new DataFrame by concatenating df_part2 with df on the "Department" column and print it
combined_df = pd.concat([df, df_part2], axis=0)
print("Concatenated DataFrame:\n", combined_df)