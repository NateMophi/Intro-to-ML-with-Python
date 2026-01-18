import pandas as pd
df = pd.read_csv("PokemonData.csv")


# # Read the headers
# print(df.columns)

# # Read each column
# print(df['Name'])
# print(df[["Name", "Speed", "Legendary"]])

# # Read each row
# print(df.iloc[1])
# print(df.iloc[1:4])

# # Read sth specific
# print(df.iloc[2,7])

# # Iterate through rows
# # for index, row in df.iterrows():
# #     print(index, row["Speed"])

# print(df.loc[df['Type1'] == "Ice"])

# # Sorting/Describing Data
# # print(df.describe())
# print(df.sort_values(["Name"], ascending=False))
# print(df.sort_values(["Type1","HP"], ascending=[0,1]))


# Making chnages to the data
# print(df.head(5))
df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["SpAtk"] + df["SpDef"] + df["Speed"]
# print(df.head(5))
df = df.drop(columns=["Total"])
# print(df.head(3))
df["Total"] = df.iloc[:, 4:10].sum(axis=1) # sum the 4th to 9th columsn horizontally
print(df.head(5))

df.to_csv("mod.csv", index=False) 

# Filtering data
print(df.loc[(df["Type1"] == "Grass") & (df["Type2"] == "Poison")])
# df.reset_index
# df.loc[df["Name"].str.contains("Mega")]
# print(df.loc[~df["Type1"].str.contains("Fire|Grass", regex=True)])
# print(df.loc[df["Name"].str.contains("^(Pi)[a-z]*", regex=True)])
# df.loc[df["Type2"]=="Poison", "Legendary"] = True

# df.loc[df["Total"] > 500, ["Generation", "Legendary"]] = ["Zero", "Unsure"]
# print(df.head())

# Grouping
sf=pd.read_csv("mod.csv")
print(sf.groupby(["Type1"])[['HP', 'Attack', 'Defense', 'SpAtk', 'SpDef', 'Speed']].mean().sort_values("Attack", ascending=False))
