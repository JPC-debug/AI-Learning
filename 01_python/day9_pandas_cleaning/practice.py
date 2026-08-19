# import pandas as pd

# data = {
#     'name': ['Jack', 'Rose', 'Tom', 'Lucy'],
#     'age' :[20, None, 21, 22],
#     'score': [90, 95, None,88]
# }

# df = pd.DataFrame(data)

# print(df)

# print(df.isnull())

# print(df.isnull().sum())

# data = {
#     'name': ['Jack', 'Rose', 'Tom', 'Lucy', 'Jack'],
#     'age': [20, 21, 21, 22, 20],
#     'score': [90, 95, 80, 88, 95]
# }

# df = pd.DataFrame(data)

# print(df)
# print(df.isnull().sum())
# print(df.dropna())

# average_age = df['age'].mean()
# df['age'] = df['age'].fillna(average_age)
# print(df)

# average_score = df['score'].mean()
# df['score'] = df['score'].fillna(average_score)
# print(df)

# print(df.duplicated())
# print(df.duplicated().sum())

# clean_df = df.drop_duplicates()
# print(clean_df)

# print(df.duplicated(subset=['name']))
# clean_df = df.drop_duplicates(subset=['name'])
# print(clean_df)

# data = {
#     'name': ['Jack', 'Rose', 'Tom', 'Lucy', 'Jack', 'Rose'],
#     'age': [20, 21, 21, 22, 20, 21],
#     'score': [90, 95, 80, 88, 95, 95]
# }

# df = pd.DataFrame(data)

# print(df.duplicated())
# print(df.duplicated().sum())

# print(df.duplicated(subset=['name']))
# print(df.duplicated(subset=['name']).sum())
# clean_df = df.drop_duplicates(subset=['name'])
# print(clean_df)



# data = {
#     'name': ['Jack', 'Rose', 'Tom', 'Lucy'],
#     'age': ['20', '21', 'unknown', '22'],
#     'score': ['90', '95', '80', '88']
# }

# df = pd.DataFrame(data)

# print(df)

# print(df.dtypes)

# df['age'] = df['age'].astype(int)
# df['age'] = pd.to_numeric(df['age'], errors='coerce')
# df['score'] = df['score'].astype(float)

# print(df.dtypes)

# print(df['score'].mean())

# data = {
#     'name': ['Jack', 'Rose', 'Tom', 'Lucy', 'Mike'],
#     'age': ['20', '21', 'unknown', '22', '19'],
#     'score': ['90', '95', '80', 'error', '85']
# }
# df = pd.DataFrame(data)

# print(df.dtypes)
# df['age'] = pd.to_numeric(df['age'], errors='coerce')
# df['score'] = pd.to_numeric(df['score'],errors='coerce')
# print(df)

# print(df.isnull().sum())

# average_age = df['age'].mean()
# df['age']=df['age'].fillna(average_age)

# average_score = df['score'].mean()
# df['score']=df['score'].fillna(average_score)

# print(df)
# print(df.isnull().sum())

# data = {
#     'name': [' Jack ', 'ROSE', ' tom', 'Lucy ', 'MIKE'],
#     'city': [' Beijing', 'SHANGHAI ', 'beijing', ' Shanghai', 'BEIJING '],
#     'score': [90, 95, 80, 88, 85]
# }

# df = pd.DataFrame(data)

# print(df)

# df['name'] = df['name'].str.strip()

# df['city'] = df['city'].str.lower().str.strip()

# data = {
#     'name': [' Jack ', 'ROSE', ' tom ', 'LUCY ', ' mike'],
#     'city': [' Beijing ', 'SHANGHAI ', 'beijing', ' Shanghai', 'BEIJING '],
#     'email': [
#         ' JACK@QQ.COM ',
#         'Rose@QQ.COM',
#         ' TOM@163.COM',
#         'lucy@GMAIL.COM ',
#         ' MIKE@QQ.COM '
#     ]
# }

# df = pd.DataFrame(data)

# df['name'] = df['name'].str.strip().str.lower()
# df['city'] = df['city'].str.strip().str.lower()
# df['email'] = df['email'].str.strip().str.lower()
# print(df)

# print(df['city'].value_counts())
import numpy as np
import pandas as pd
data = {
    'name': ['Jack', 'Rose', 'Tom', 'Lucy', 'Mike', 'John'],
    'age': [20, 21, 150, 22, -5, 19],
    'score': [90, 105, 80, 88, -20, 95]
}

df = pd.DataFrame(data)

print(df[(df['age'] <= 0) | (df['age'] >= 100)])
print(df[~df['score'].between(0,100)])


df.loc[(df['age'] <= 0) | (df['age'] >= 100),'age'] = np.nan
df.loc[~df['score'].between(0,100),'score'] = np.nan

average_age = df['age'].mean()
df['age'] = df['age'].fillna(average_age)

average_score = df['score'].mean()
df['score'] = df['score'].fillna(average_score)

print(df)