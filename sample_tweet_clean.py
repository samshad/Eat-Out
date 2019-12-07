import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
#nltk.download('stopwords')
#nltk.download('punkt')


def filter_moyla(moyla_list):
    for i in range(len(moyla_list)):
        moyla_list[i] = re.sub(r'https://[A-Za-z0-9].co/[A-Za-z0-9]+', '', moyla_list[i])
        moyla_list[i] = re.sub(r'http://[A-Za-z0-9].co/[A-Za-z0-9]+', '', moyla_list[i])
        moyla_list[i] = re.sub(r'[^\x00-\x7f]', r'', moyla_list[i])
        moyla_list[i] = re.sub(r'@[A-Za-z0-9]+', '', moyla_list[i])
        moyla_list[i] = re.sub(r'RT', '', moyla_list[i])
        moyla_list[i] = re.sub(r"^.*\b(I'm at)\b.*$", '', moyla_list[i])

        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(moyla_list[i])
        tweet_lst = []

        for x in word_tokens:
            if x not in stop_words:
                tweet_lst.append(x)

        moyla_list[i] = " ".join(tweet_lst)

    return moyla_list


df = pd.read_csv('Sample Datas/_greeneyedlady_.csv')
ls = filter_moyla(list(df.tweet))
arr = []
for i in ls:
    if len(i) > 0:
        arr.append(i)
af = pd.DataFrame(arr, columns=['tweet'])
af.to_csv('Sample Datas/demotweet.csv', index=False)
