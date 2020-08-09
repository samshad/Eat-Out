import tweepy
import json
import os
import pandas as pd


access_key = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

df = pd.read_csv('Data/userlist.csv')
users = list(df.users)
cnt = 0
users.sort()

for user in users:
    print(user)
    cnt += 1
    print('Count: ', str(cnt))
    name = user
    tweet_objects = []
    alltweets = []
    new_tweets = api.user_timeline(screen_name=name, count=200)
    
    for i in new_tweets:
        tweet_objects.append(i)
    
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
    
    for i in tweet_objects:
        path = 'Tweet_Objects/' + name + '/'
        if not os.path.exists(path):
            os.makedirs(path)
    
        with open(path + i.id_str + '.json', 'w', encoding='utf-8') as f:
            json.dump(i._json, f, ensure_ascii=False, indent=4)

print("done...")
