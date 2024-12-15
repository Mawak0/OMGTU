import pandas as pd

#3
df = pd.read_csv(r"C:\Users\Пользователь\code\OMGTU\PR\Term3\PhiUSIIL_Phishing_URL_Dataset.csv")
pd.set_option('display.width', 0)
pd.set_option('display.max_columns', None)
print(df.head())
print(df.tail())
df.info()
print(df.describe())
