import pandas as pd


#1
df1 = pd.DataFrame({
  'Name': ['Strom, Mrs. Wilhelm (Elna Matilda Persson)', 'Navratil, Mr. Michel (Louis MHoffman)', 'Minahan, Miss. Daisy E'],
  'Age': [29, 36.5, 33],
  'Sex': ['female', 'male', 'female']
})

#2
df2 = pd.read_csv('titanic_csv.csv', sep=';')

#3
df3 = pd.read_csv('https://gist.githubusercontent.com/zaryanezrya/8b4ef51c707cb16d5e88a44dc00a1bb2/raw/41230f49c6268e072dbf102672f670be256922ab/gistfile1.txt')

#4
df4 = pd.concat([df2, df3])
df4.drop_duplicates(inplace=True)

#5
df4.set_index('passengerid', inplace=True)
df4.sort_index(inplace=True)

#6
df4.info()
print(df4.describe())



