import os
import pandas as pd
import json


def write_file(user, year, data, fname):
    p = 'Data/Grouped_Tweets/' + user + '/' + year + '/'
    if not os.path.exists(p):
        os.makedirs(p)
    dataframe = pd.DataFrame(data, columns=['id', 'date', 'tweet'])
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe.sort_values(by=['date'], inplace=True, ascending=False)
    dataframe.to_csv('Data/Grouped_Tweets/' + user + '/' + year + '/' + fname + '.csv', index=None, header=True)


def getData(user, year, mn, mx, q):
    df = pd.read_csv('Data/Initial_Tweet_Texts/' + user + '.csv')
    arr = []
    for index, row in df.iterrows():
        m = int(row['date'].split('-')[1])
        y = row['date'].split('-')[0]
        if mn <= m <= mx and year == y:
            arr.append([row['id'], row['date'], row['tweet']])
    write_file(user, year, arr, q)


with open('Data/timeframe.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

for user in data:
    print(user)
    p = 'Data/Grouped_Tweets/' + user + '/'
    if not os.path.exists(p):
        os.makedirs(p)
    for year in data[user]:
        for q in data[user][year]:
            if q == 'Q1':
                getData(user, year, 1, 4, q)
            if q == 'Q2':
                getData(user, year, 5, 8, q)
            if q == 'Q3':
                getData(user, year, 9, 12, q)

print('Done...')
