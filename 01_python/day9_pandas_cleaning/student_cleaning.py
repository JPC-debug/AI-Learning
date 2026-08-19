import pandas as pd
import numpy as np

df = pd.read_csv('students_dirty.csv')

# print(df)

# df.info()

# print(df.isnull().sum())
# print(df.duplicated().sum())

df['name'] = df['name'].str.strip().str.lower()
df['city'] = df['city'].str.strip().str.lower()

df['age'] = pd.to_numeric(df['age'],errors='coerce')
df['score'] = pd.to_numeric(df['score'],errors='coerce')

df = df.drop_duplicates()

# print(df)

# print(df.dtypes)

# print(df.isnull().sum())

# print(df.duplicated().sum())

df.loc[(df['age'] <= 0) | (df['age'] >= 100), 'age'] = np.nan
df.loc[~df['score'].between(0,100),'score'] = np.nan

average_age = df['age'].mean()
df['age'] = df['age'].fillna(average_age)

average_score = df['score'].mean()
df['score'] = df['score'].fillna(average_score)

# print(df)

# print("\n缺失值：")
# print(df.isnull().sum())

# print("\n重复数据：")
# print(df.duplicated().sum())

# print("\n数据类型：")
# print(df.dtypes)

# print(df['city'].value_counts())

print("\n清洗后的数据：")
print(df)

print("\n缺失值：")
print(df.isnull().sum())

print("\n重复数据数量：")
print(df.duplicated().sum())

print("\n数据类型：")
print(df.dtypes)

print("\n城市分布：")
print(df['city'].value_counts())

print(f"所有学生的平均成绩：{df['score'].mean().round(2)}")
print(f'最高成绩：{df["score"].max()}')
print(f'最低成绩：{df["score"].min()}')

df = df.sort_values('score',ascending=False)
df = df.reset_index(drop=True)
df['rank'] = df.index + 1

print(df)

df.to_csv('students_cleaned.csv', index=False)