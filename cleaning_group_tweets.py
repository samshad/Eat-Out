import pandas as pd
import re
import json
import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')


def filter_moyla(tweets_list):
    for i in range(len(tweets_list)):
        tweets_list[i] = re.sub(r'https://[A-Za-z0-9].co/[A-Za-z0-9]+', '', tweets_list[i])
        tweets_list[i] = re.sub(r'http://[A-Za-z0-9].co/[A-Za-z0-9]+', '', tweets_list[i])
        tweets_list[i] = re.sub(r'[^\x00-\x7f]', r'', tweets_list[i])
        tweets_list[i] = re.sub(r'@[A-Za-z0-9]+', '', tweets_list[i])
        tweets_list[i] = re.sub(r'RT', '', tweets_list[i])
        tweets_list[i] = re.sub(r"^.*\b(I'm at)\b.*$", '', tweets_list[i])

        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(tweets_list[i])
        tweet_lst = []

        for x in word_tokens:
            if x not in stop_words:
                tweet_lst.append(x)

        tweets_list[i] = " ".join(tweet_lst)

    return tweets_list


with open('Data/timeframe.json', encoding='utf-8') as json_file:
    users = json.load(json_file)

for user in users:
    print(user)
    for year in users[user]:
        for q in users[user][year]:
            path = 'Data/Grouped_Tweets/' + user + '/' + year + '/'
            df = pd.read_csv(path + q + '.csv')
            t_list = filter_moyla(list(df.tweet))
            arr = []
            for t in t_list:
                if len(t) > 0:
                    arr.append(t)
            tf = pd.DataFrame(arr, columns=['tweet'])
            tf.to_csv(path + q + '_tweets_cleaned.csv', index=False)
