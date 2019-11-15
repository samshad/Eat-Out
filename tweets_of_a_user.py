import tweepy
import pandas as pd
import csv
import sys
import time
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')
import json
import os


access_key = "1155844358043652096-iJtClkifFAtl1EgdCVexEhD9hAyw9F"
access_secret = "votFnHMkt3XiBfUbQz6pfWwDnKg5wbQDLeJf8QsIiAGUJ"
consumer_key = "n6JuZxpbm9fLjfJH8tOFE7Gyy"
consumer_secret = "odWOvaXxREpMEcPvpuRwr4inSGJB3zhRCQtFHLdVQDij325kX1"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


name = 'DidiMo1313'

def filter_moyla(moyla_list):
    for i in range(len(moyla_list)):
        #moyla_list[i] = re.sub(r'https://[A-Za-z0-9].co/[A-Za-z0-9]+', '', moyla_list[i])
        #moyla_list[i] = re.sub(r'http://[A-Za-z0-9].co/[A-Za-z0-9]+', '', moyla_list[i])
        moyla_list[i] = re.sub(r'[^\x00-\x7f]', r'', moyla_list[i])
        #moyla_list[i] = re.sub(r'@[A-Za-z0-9]+', '', moyla_list[i])
        #moyla_list[i] = re.sub(r'[b"]', '', moyla_list[i])

        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(moyla_list[i])
        tweet_lst = []

        for x in word_tokens:
            if x not in stop_words:
                tweet_lst.append(x)

        moyla_list[i] = " ".join(tweet_lst)

    return moyla_list


tweet_objects = []
alltweets = []
new_tweets = api.user_timeline(screen_name=name, count=200)

"""for i in new_tweets:
    print(i.id)
    print(i._json)

    path = 'Tweet_Objects/' + name + '/'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + i.id_str + '.json', 'w', encoding='utf-8') as f:
        json.dump(i._json, f, ensure_ascii=False, indent=4)"""

for i in new_tweets:
    tweet_objects.append(i)

#tweet_texts = filter_moyla(tweet_texts)
alltweets.extend(new_tweets)
oldest = alltweets[-1].id - 1
while len(new_tweets) > 0:
    print("getting tweets before %s" % (oldest))
    new_tweets = api.user_timeline(screen_name=name, count=200, max_id=oldest)
    for i in new_tweets:
        tweet_objects.append(i)
    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1
    print("...%s tweets downloaded so far" % (len(alltweets)))

print(len(tweet_objects))
for i in tweet_objects:
    path = 'Tweet_Objects/' + name + '/'
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + i.id_str + '.json', 'w', encoding='utf-8') as f:
        json.dump(i._json, f, ensure_ascii=False, indent=4)


#tweet_texts = filter_moyla(tweet_objects)
#outtweets = [i.encode("utf-8") for i in tweet_texts]
#print(type(outtweets))

#dataframe = pd.DataFrame(outtweets, columns=['tweets'])
#to_csv = dataframe.to_csv('Tweets/' + name + '.csv', index=None, header=True)

# time.sleep(5)

print("done...")