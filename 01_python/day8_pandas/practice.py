import pandas as pd

students = {
    'name': ['Jack', 'Rose', 'Tom'],
    'age': [20, 21, 19],
    'score': [85, 92, 78]
}

df = pd.DataFrame(students)

print(df)

products = {
    'product': ['Apple', 'Banana','Orange'],
    'price': [5, 3, 4],
    'stock': [100, 150, 80]
}
product_df = pd.DataFrame(products)
print(product_df)   

# print(df.head())
# print(df.head(2))
# print(df.tail())
# print(df.tail(2))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)

# print(product_df.shape[0])
# print(product_df.shape[1])

# print(df['name'])
# print(df['score'])

# print(type(df))
# print(type(df['score']))

# print(df[['name','score']])

# print(df.loc[1,'score'])
# print(df.iloc[1,2])

# print(product_df['price'])
# print(product_df[['product', 'stock']])
# print(product_df.loc[1])
# print(product_df.loc[1,'stock'])
# print(product_df.iloc[2,1])

# print(type(product_df['price']))
# print(type(product_df[['price']]))

# print(product_df[product_df['price'] > 3])
# print(product_df[product_df['stock'] >= 100])
# print(product_df[(product_df['price'] >= 4) & (product_df['stock'] >= 80)])
# print(product_df[(product_df['price'] < 4) | (product_df['stock'] < 100)])
# print(product_df.loc[
#     product_df['stock'] >= 100,
#     ['product','stock']
# ])

product_df['value'] = product_df['price'] * product_df['stock']
print(product_df)
print(product_df['price'].mean())
print(product_df['price'].max())
print(product_df['price'].min())
print(product_df['stock'].sum())
print(product_df['value'].sum())
print(product_df.loc[product_df['value'].idxmax()])