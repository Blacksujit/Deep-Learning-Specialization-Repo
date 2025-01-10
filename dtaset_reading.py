import pandas as pd
import numpy as np

# Load the dataset
dftrain = pd.read_csv('data.csv')
dfeval = pd.read_csv('eval.csv')

# Display the first few rows of dftrain
print(dftrain.head())

# Pop the 'Health Index' column from dftrain and assign it to y_train
y_train = dftrain.pop('Age')
# Display the first few rows of dftrain after popping the 'Health Index' column
print(dftrain.head())

# Pop the 'Health Index' column from dfeval and assign it to y_eval
y_eval = dfeval.pop('Health Index')

# Display the first few rows of dfeval after popping the 'Health Index' column
print(dfeval.head())

print("\n----------------------------\n")

# print(y_train)
print("\n----------------------------\n")

print("\n----------------------------\n")
print(dftrain.loc[0] , y_train.loc[0])

print("\n----------------------------\n")


print(dftrain.describe())

print("\n----------------------------\n")
print(dftrain.shape)
print("\n----------------------------\n")

print(dftrain.Name.hist(bins=20))




