import pandas as pd
import json
import os


with open('Data/timeframe.json', encoding='utf-8') as json_file:
    users = json.load(json_file)

st = set()
cnt = 0
for user in users:
    for year in users[user]:
        for q in users[user][year]:
            path = 'Data/Grouped_Tweets/' + user + '/' + year + '/'
            df = pd.read_csv(path + q + '_tweets_cleaned.csv')
            t_list = list(df.tweet)
            if len(t_list) < 10:
                st.add(user)
                cnt += 1
                #print(user, year, q, len(t_list))

ls = list(st)
ls.sort()
print(len(st), cnt)
