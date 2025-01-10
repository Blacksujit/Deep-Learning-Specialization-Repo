import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dataset = pd.read_csv("C:\\Users\\HP\\Downloads\\archive (6)\\loan_data_set.csv")


df = dataset 

df.head(4)

df.isnull().sum()

print(df.isnull().sum())




