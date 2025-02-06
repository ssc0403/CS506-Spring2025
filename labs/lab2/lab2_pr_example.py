import numpy as np 
import pandas as pd 

f = open("lab2.txt", "w")

# Your goal is to find the top 5 cheapest houses near the 
# "Beach" and print them in ascending order by price.

f.write("Find the top 5 cheapest houses near the 'Beach' and print them in ascending order by price. \n\n")

airbnb_data = [
    {"HouseID": 101, "Location": "Beach",       "Price": 120, "Bedrooms": 2},
    {"HouseID": 102, "Location": "Beach",       "Price": 90,  "Bedrooms": 1},
    {"HouseID": 103, "Location": "City Center", "Price": 150, "Bedrooms": 3},
    {"HouseID": 104, "Location": "Beach",       "Price": 200, "Bedrooms": 4},
    {"HouseID": 105, "Location": "Suburbs",     "Price": 75,  "Bedrooms": 1},
    {"HouseID": 106, "Location": "Beach",       "Price": 140, "Bedrooms": 2},
    {"HouseID": 107, "Location": "City Center", "Price": 190, "Bedrooms": 3},
    {"HouseID": 108, "Location": "Beach",       "Price": 60,  "Bedrooms": 1},
    {"HouseID": 109, "Location": "Suburbs",     "Price": 85,  "Bedrooms": 2},
    {"HouseID": 110, "Location": "Beach",       "Price": 130, "Bedrooms": 2},
]

# Load the data into a DataFrame
df = pd.DataFrame(airbnb_data)
print("Original DataFrame:\n")
print(df)
print()

f.write("Original DataFrame:\n")
f.write(df.to_string())
f.write("\n\n")

# Filter every Beach Location

filtered_df = df[df["Location"] == "Beach"] # splicing df based on Location

print("Beach houses filtered:\n")
print(filtered_df)
print()

f.write("Beach houses filtered:\n")
f.write(filtered_df.to_string())
f.write("\n\n")

# Sort in ascending order by price

sorted_df = filtered_df.sort_values(by="Price") # sort Price values

print("Beach houses sorted in ascending order by price:\n")
print(sorted_df)
print()

f.write("Beach houses sorted in ascending order by price:\n")
f.write(sorted_df.to_string())
f.write("\n\n")

# Take the top 5

top_df = sorted_df.head(5) # head shows the top 5 rows

print("Top 5 cheapest Beach Houses:\n")
print(top_df)
print()

f.write("Top 5 cheapest Beach Houses:\n")
f.write(top_df.to_string())
f.write("\n\n")

f.close()