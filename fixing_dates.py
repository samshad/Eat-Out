import pandas as pd
import os
import json


month = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
    'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

obj_path = 'Data/Tweet_Objects/'
files = os.listdir('Data/Foursq_Data/')
files.sort()

for file in files:
    print(file)
    username = file.split('.csv')[0]
    df = pd.read_csv('Data/Foursq_Data/' + file)
    arr = []

    for index, row in df.iterrows():
        tid = str(row['tweet_id'])

        with open('Data/Tweet_Objects/' + username + '/' + tid + '.json', encoding='utf-8') as json_file:
            data = json.load(json_file)

        date = data['created_at'].split(' ')[5] + '-' + str(month[data['created_at'].split(' ')[1]]) + '-' + data['created_at'].split(' ')[2]
        arr.append([tid, date, row['title'], row['category'], row['rating'], row['urls']])

    dataframe = pd.DataFrame(arr, columns=['tweet_id', 'date', 'title', 'category', 'rating', 'urls'])
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe.sort_values(by=['date'], inplace=True, ascending=False)
    dataframe.to_csv('Data/Final_Foursq_Data/' + username + '.csv', index=None, header=True)

print('Done...')