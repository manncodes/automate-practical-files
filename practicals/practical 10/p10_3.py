import pandas as pd

# pandas dataframe from python dictoionary
dict = {"Name": ["Tom", "Jack", "Steve", "Ricky"], "Age": [28, 34, 29, 42]}
df = pd.DataFrame(dict)
print(df)

# pandas dataframe from CSV file
df = pd.read_csv("practical 10/addr.csv")
print(df)


# pandas dataframe from JSON file
df = pd.read_json("practical 10/addr.json")
print(df)

# store dataframe in pickle format
df.to_pickle("practical 10/p10_3.pkl")
