import os
import pandas as pd


df = pd.read_csv('Saved Datas/Restaurants.csv')

print(len(df.urls))
df = df.drop_duplicates('urls')
print(len(df.urls))