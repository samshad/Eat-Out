import pandas as pd
import os


path = 'Data/Grouped_Datas/'
users = os.listdir(path)
q_count = []
count = 0

for user in users:
    years = os.listdir(path + user)
    for year in years:
        q1 = pd.read_csv(path + user + '/' + year + '/' + 'Q1.csv')
        q2 = pd.read_csv(path + user + '/' + year + '/' + 'Q2.csv')
        q3 = pd.read_csv(path + user + '/' + year + '/' + 'Q3.csv')
        count += (len(q1['tweet_id']) + len(q2['tweet_id']) + len(q3['tweet_id']))
        if len(q1['tweet_id']) > 0:
            q_count.append(len(q1['tweet_id']))
        if len(q2['tweet_id']) > 0:
            q_count.append(len(q2['tweet_id']))
        if len(q3['tweet_id']) > 0:
            q_count.append(len(q3['tweet_id']))

print(count)
print('Average Check in by USERS: ' + str(count / 200))
print(len(q_count))
print('AverageCheck in by USERS')


