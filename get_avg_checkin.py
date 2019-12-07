import pandas as pd
import os


path = 'Data/Grouped_Datas/'
users = os.listdir(path)
q_count = []
count = 0

for user in users:
    years = os.listdir(path + user)
    for year in years:
        files = os.listdir(path + user + '/' + year + '/')
        for file in files:
            df = pd.read_csv(path + user + '/' + year + '/' + file)
            count += len(df['tweet_id'])
            q_count.append(len(df['tweet_id']))

print(count)
print('Average Check in by USERS: ' + str(count / 200))
print(len(q_count))
print(q_count)
df = pd.DataFrame(q_count, columns=['count'])
print(df.describe())
