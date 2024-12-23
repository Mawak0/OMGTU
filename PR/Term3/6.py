import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import normaltest

#3
df = pd.read_csv(r"PhiUSIIL_Phishing_URL_Dataset.csv")
pd.set_option('display.width', 0)
pd.set_option('display.max_columns', None)
print(df.head())
print(df.tail())
df.info()
print(df.describe())
df.drop_duplicates(inplace=True)

#4
df.rename(columns={"URL": "WebsiteURL"}, inplace=True)

#5
#Гистограмма распределения
plt.figure(figsize=(10, 6))
plt.hist(df['URLLength'], bins=600, color='blue', alpha=0.7, range=(0, 600))
plt.title('Распределение длины URL')
plt.xlabel('Длина URL')
plt.ylabel('Частота')
plt.savefig('histogram_url_length.png')
plt.show()

#Диаграмма "ящик с усами"
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['DomainLength'])
plt.title('Ящик с усами для длины домена')
plt.ylabel('Длина домена')
plt.savefig('boxplot_domain_length.png')
plt.show()

#Круговая диаграмма
values = df['IsHTTPS'].value_counts()
labels = values.index
plt.figure(figsize=(8, 8))
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['green', 'red'])
plt.title('Распределение HTTPS')
plt.savefig('piechart_https.png')
plt.show()

#Тепловая карта корреляций
plt.figure(figsize=(50, 50))
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', linewidths=0.5)
plt.title('Тепловая карта корреляций')
plt.savefig('heatmap_correlations.png')
plt.show()

#Countplot для двух номинативных признаков
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='IsHTTPS', hue='HasObfuscation', palette='Set2')
plt.title('Распределение HTTPS и Obfuscation')
plt.xlabel('HTTPS')
plt.ylabel('Количество')
plt.savefig('countplot_https_obfuscation.png')
plt.show()

#6
for col in df.columns:
    if df[col].isnull().any():
        if df[col].dtype == 'int64':
            df[col].fillna(df[col].median(), inplace=True)
        elif df[col].dtype == 'float64':
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

#7
sample_data = df['URLLength'].sample(n=200)
stat, p_value = normaltest(sample_data)
print(f"Статистика: {stat}, p-значение: {p_value}")
if p_value < 0.05:
    print(f"Распределение столбца 'URLLength' не является нормальным.")
else:
    print(f"Распределение столбца 'URLLength' является нормальным.")


#8
categorical_columns = ['TLD', 'IsDomainIP', 'HasObfuscation', 'IsHTTPS', 'HasTitle', 'HasFavicon', 'IsResponsive', 'HasDescription', 'HasSocialNet', 'HasPasswordField']
df = pd.get_dummies(df, columns=categorical_columns)

#9
output_path = r"Preprocessed_Dataset.csv"
df.to_csv(output_path, index=False)
