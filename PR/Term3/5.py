import pandas as pd


#1
df1 = pd.DataFrame({
  'name': ['Strom, Mrs. Wilhelm (Elna Matilda Persson)', r'Navratil, Mr. Michel ("Louis M Hoffman")', 'Minahan, Miss. Daisy E'],
  'age': [29, 36.5, 33],
  'sex': ['female', 'male', 'female']
})

#2
df2 = pd.read_csv('titanic_csv.csv', sep=';')

#3
df3 = pd.read_csv('https://gist.githubusercontent.com/zaryanezrya/8b4ef51c707cb16d5e88a44dc00a1bb2/raw/41230f49c6268e072dbf102672f670be256922ab/gistfile1.txt')

#4
df2.columns = df2.columns.str.lower()
df3.columns = df3.columns.str.lower()
df4 = pd.concat([df2, df3])
df4.drop_duplicates(inplace=True)

#5
df4.set_index('passengerid', inplace=True)
df4.sort_index(inplace=True)

#6
df4.info()
print(df4.describe())

#7
#print("--------------------------")
df4.iloc[0], df4.loc[2] = df4.loc[2], df4.iloc[0]
#print(df4.iloc[0])

#8
def f(a):
  if a == "female": return "f"
  if a == "male": return "m"

df4["sex"] = df4["sex"].map(f)

#9
print("Билеты, по которым плыло 6 и более человек:")
b1 = df4.groupby(by="ticket")["ticket"].count()
b2 = b1[b1 >= 6].index
for ticket in b2:
  print(ticket)
  print(df4[df4['ticket'] == ticket]["name"])
print("--------------------------------------------")

#10
filtered_df = df4[df4['name'].isin(df1["name"])]
#print(filtered_df["cabin"])
print(df4[df4['cabin'].isin(filtered_df["cabin"])]["name"])

#11
df4["BirthYear"] = 1912 - df4["age"]

#12
g1 = df4.groupby(by="cabin")["cabin"].count()
df4["Companion"] = df4["cabin"].map(g1) - 1
print(df4)

#13
df4.iloc[0], df4.loc[1] = df4.loc[1], df4.iloc[0]

#14
df4.to_csv("output.csv")

#15
print("Топ 10 людей, которые больше всех заплптили за билет:")
top_10 = df4.nlargest(10, "fare")
print(top_10)

#16
print(df4.groupby(['sex', 'survived'])["name"].count())

#17
print(df4.groupby(['pclass', 'survived'])["name"].count())
