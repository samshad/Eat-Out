import pandas as pd
import os
import json


month = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

dataframe = pd.read_csv('Data/userlist.csv')
users = list(dataframe.users)
users.sort()
cnt = 0

for user in users:
    cnt += 1
    print('Count: ' + str(cnt) + ' ===> ' + user)
    path = 'Data/Tweet_Objects/' + user + '/'
    files = os.listdir(path)
    arr = []
    username = user

    for file in files:
        with open(path + file, encoding='utf-8') as json_file:
            data = json.load(json_file)

        date = data['created_at'].split(' ')[5] + '-' + str(month[data['created_at'].split(' ')[1]]) + '-' + data['created_at'].split(' ')[2]
        arr.append([data['id_str'], date, data['text']])

    df = pd.DataFrame(arr, columns=['id', 'date', 'tweet'])
    path = 'Data/Initial_Tweet_Texts/'
    df['date'] = pd.to_datetime(df['date'])
    df.sort_values(by=['date'], inplace=True, ascending=False)
    df.to_csv(path + username + '.csv', index=False)

print('Done')