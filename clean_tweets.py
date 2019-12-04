import ast
import csv
from csv import DictWriter
import re
import pandas as pd
import demoji
import os

demoji.download_codes()  # for downloading demoji cache

df = pd.read_csv("Data/Found_Data/arifhosentamim.csv")
result = ""
read = ""
f = open("insomnia_no_usa_output.csv", "w", newline='', encoding='utf-8')
fieldnames = ['tweet_id', 'label', 'tweets']
writer: DictWriter = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()

files = os.listdir("Data/Found_Data/")
print(files)
for file in files:
    data = pd.read_csv("Data/Found_Data/" + file)
    tweet = []
    for index, row in data.iterrows():
        row['tweet'] = ast.literal_eval(row['tweet'])
        row['tweet'] = (row['tweet'].decode() if isinstance(row['tweet'], bytes) else row['tweet']).strip()
        row[2] = re.sub(r'@\S+', '', row[2])  # Remove mentions
        row[2] = re.sub(r'#\S+', '', row[2])  # Remove hashtags
        row[2] = re.sub(r'RT', '', row[2])
        row[2] = re.sub(r'http\S+', '', row[2])  # Remove urls
        row[2] = re.sub(r'www\S+', '', row[2])

        try:
            for x, y in demoji.findall(row[2]).items():
                row[2] = row[2].replace(x, " " + y)
        except ValueError as e:
            print(e)

        row[2] = row[2].strip()
        #print(len(row[2]))
        tweet.append(row[2])
    seperator = " "
    content = seperator.join(tweet)
    file = file.split(".csv")[0]
    f = open("Data/Tweet_Text_Files/" + file + ".txt", "w+", encoding="utf-8")
    f.write(content)
    f.close()
    print("done............................................................")