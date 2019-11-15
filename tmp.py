import pandas as pd


df = pd.read_csv('Saved Datas//All_Restaurant_Data.csv')

x = df[df.url == 'https://foursquare.com/v/pollo-tropical/4becafbbbbe62d7f45457f2b']

print(len(x.url))