import os
import pandas as pd
import json


path = 'Data/Grouped_Datas/'
users = os.listdir(path)

timeframe = {}
for user in users:
    timeframe[user] = dict()
    years = os.listdir(path + user + '/')
    for y in years:
        timeframe[user][y] = []
        qs = os.listdir(path + user + '/' + y + '/')
        for q in qs:
            timeframe[user][y].append(q.split('.csv')[0])
    print(timeframe)

with open('Data/timeframe.json', 'w') as outfile:
    json.dump(timeframe, outfile, indent=4)
