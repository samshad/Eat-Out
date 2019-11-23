import pandas as pd
import os


path = 'Data/Foursq_Data/'
files = os.listdir(path)
x = []

for file in files:
    df = pd.read_csv(path + file)
    for i in df.date:
        x.append(int(i.split('-')[0]))
    x = list(set(x))

x.sort()
print(x)
