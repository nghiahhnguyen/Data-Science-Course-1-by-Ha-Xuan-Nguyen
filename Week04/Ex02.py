import pandas as pd
#load data
df = pd.read_csv("iris.txt")
#statistics description
print('sepal length')
sl = df.sepal_length
sc = df['species']
print(sl.groupby(sc).describe())

print("\nsepal width")
sl=df.sepal_width
print(sl.groupby(sc).describe())

print("\npetal length")
sl=df.petal_length
print(sl.groupby(sc).describe())

print("\npetal width")
sl=df.petal_width
print(sl.groupby(sc).describe())

# normalization

# distance
d=float(input("Enter a distance: "))
m=df.sepal_length.groupby(df["species"]).mean()

df.loc[((abs(df.sepal_length - m['setosa']) > d) & (df.species == 'setosa')), 'sepal_length'] = (df.sepal_length + m['setosa'])/2
df.loc[((abs(df.sepal_length - m['versicolor']) > d) & (df.species == 'versicolor')), 'sepal_length'] = (df.sepal_length + m['versicolor'])/2
df.loc[((abs(df.sepal_length - m['virginica']) > d) & (df.species == 'virginica')), 'sepal_length'] = (df.sepal_length + m['virginica'])/2
print(df)