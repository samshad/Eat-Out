import pandas as pd
import os


path = 'Data/Foursq_Data/'
files = os.listdir(path)
files.sort()

user = files[0]

years = []

df = pd.read_csv(path + user)

for i in df.date:
    y = i.split('-')[0]
    years.append(y)

years = list(set(years))

for i in years:
    p = 'Data/Grouped_Datas/' + user.split('.csv')[0] + '/' + i + '/'
    if not os.path.exists(p):
        os.makedirs(p)

one = []
two = []
three = []

for index, row in df.iterrows():
    y = int(row['date'].split('-')[1])
    if y <= 4:
        one.append([row['tweet_id'], row['date'], row['title'], row['category'], row['rating'], row['urls']])
    elif y <= 8:
        two.append([row['tweet_id'], row['date'], row['title'], row['category'], row['rating'], row['urls']])
    else:
        three.append([row['tweet_id'], row['date'], row['title'], row['category'], row['rating'], row['urls']])

print(one)

dataframe = pd.DataFrame(one, columns=['tweet_id', 'date', 'title', 'category', 'rating', 'urls'])
dataframe['date'] = pd.to_datetime(dataframe['date'])
dataframe.sort_values(by=['date'], inplace=True, ascending=False)
dataframe.to_csv('Data/Grouped_Datas/50centwingnight/2019' + 'one.csv', index=None, header=True)

'''for index, row in df.iterrows():
    y = row['date'].split('-')[0]
    years[y].append(row)

path = 'Tweet_Objects/' + name + '/'
        if not os.path.exists(path):
            os.makedirs(path)

print(years)'''
