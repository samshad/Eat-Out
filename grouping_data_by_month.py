import pandas as pd
import os


def write_file(username, year, data, fname):
    dataframe = pd.DataFrame(data, columns=['tweet_id', 'date', 'title', 'category', 'rating', 'urls'])
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe.sort_values(by=['date'], inplace=True, ascending=False)
    dataframe.to_csv('Data/Grouped_Datas/' + username + '/' + year + '/' + fname + '.csv', index=None, header=True)


path = 'Data/Foursq_Data/'
files = os.listdir(path)
files.sort()

for file in files[3:]:
    username = file.split('.csv')[0]
    print(username)
    years = []

    df = pd.read_csv(path + file)

    for i in df.date:
        y = i.split('-')[0]
        years.append(y)

    years = list(set(years))

    for i in years:
        p = 'Data/Grouped_Datas/' + username + '/' + i + '/'
        if not os.path.exists(p):
            os.makedirs(p)

    for year in years:
        one = []
        two = []
        three = []

        for index, row in df.iterrows():
            m = int(row['date'].split('-')[1])
            y = row['date'].split('-')[0]
            if m <= 4 and year == y:
                one.append([row['tweet_id'], row['date'], row['title'], row['category'], row['rating'], row['urls']])
            elif m <= 8 and year == y:
                two.append([row['tweet_id'], row['date'], row['title'], row['category'], row['rating'], row['urls']])
            elif m <= 12 and year == y:
                three.append([row['tweet_id'], row['date'], row['title'], row['category'], row['rating'], row['urls']])

        write_file(username, year, one, 'first')
        write_file(username, year, two, 'second')
        write_file(username, year, three, 'third')

print('Done')
