import utils.session
import pandas as pd

# df = pd.read_csv("C:/Users/PC/Downloads/ml.csv")
# print(df.shape)
# print(df.describe())
# print(df.isnull().sum())
# print(df.head())
# print(df.dtypes)

# print(df.info())
# print(df.columns)


# print("one hot encoded data frame")

# one_hot_encoded_df =pd.get_dummies(df, columns= ["owner_district"])
# print(one_hot_encoded_df.columns)

"""from sklearn.preprocessing import LabelEncoder

data = {
    'color': ['red', 'green', 'blue','red'],
    'owner_district': ['A', 'A', 'B','A'],
    'price': [100, 200, 300,200],
    'height': [1.5, 1.8, 2.0,5],
    'weight': [60, 70, 80,50],
    'targets': [1,0,1,0],
    

}
df2 = pd.DataFrame(data)
print(df2.columns)"""

"""#1 one hot encodding
one_hot_encoded_df2 = pd.get_dummies(df2, columns= ["owner_district","color","price","height","weight"])
one_hot_encoded_df2 = one_hot_encoded_df2.astype(int)

print("one hot encoded data frame")
print(one_hot_encoded_df2.columns)
print(one_hot_encoded_df2)"""

"""label_encoder = LabelEncoder()
encoded_df2 = label_encoder.fit_transform(df2['owner_district'])
print(encoded_df2)"""

"""freq=  df2['color'].value_counts(normalize=True)
df2['color_freq'] = df2['color'].map(freq)
print(df2)
# df2.drop(2, axis=0, inplace=True)
df2.drop('color', axis=1, inplace=True)
print(df2)"""
"""
from category_encoders import BinaryEncoder
encoder = BinaryEncoder(cols='color')
encoded_Data = df.fit_transform(df2['color'])"""

"""from category_encoders import  TargetsEncoder
encoder = TargetsEncoder(cols=['color'])
data = encoder.fit_transform(df2['color'],df2['Target'])
print(data)"""
"""print("Description")
print(df2.describe())

print(df2.loc[2])
print(df2.iloc[2])

print("after grouping by owner district")
df2 = df2.groupby('owner_district')['weight'].sum()
print(df2)"""

"""import numpy as np
file = np.genfromtxt("C:/Users/PC/Downloads/ml.csv",delimiter = ",")
df = pd.DataFrame(file)
print(df.shape)
print(df.describe)"""
"""
from scipy import loadtxt
dataf = pd.DataFrame(np.loadtxt("C:/Users/PC/Downloads/ml.csv",delimiter =','))
"""
# from sklearn.datasets import load_iris
# data = load_iris()
# print(data)

from sklearn.linear_model import LinearRegression
data ={"X":[1,2,3,4,5], "Y":[2,None,6,8,10]}
df = pd.DataFrame(data)


train = df[df['Y'].notnull()]
# print (train)
x_train =train[['X']]
y_train =train['Y']
print (x_train,y_train)

model = LinearRegression()
model.fit(x_train,y_train)

missing = df[df['Y'].isnull()]
x_missing = missing[["X"]]
print("y that does not have x")
print(df.loc[df['Y'].isnull(),"Y"])
df.loc[df['Y'].isnull(),"Y"] =model.predict(x_missing)
print(df.head())
print (missing)

"""data = {
    'color': ['redeeeeee', 'Green', 'bluecee','red'],
    'owner_district': ['A', 'a', 'B','c'],
    'price': [100, 200, 300,200],
    'height': [1.5, 1.8, 2.0,5],
    'weight': [60, 70, 80,50],
    'targets': [1,0,1,0],
    

}

sorted_weight = sorted(data['color'], key=lambda x : len(x))
print(sorted_weight)
colors = sorted(data['owner_district'])
print(colors)
"""