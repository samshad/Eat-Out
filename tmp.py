import os
import pandas as pd


path = 'Data/Foursq_Data/'
files = os.listdir(path)
dataframe = pd.DataFrame(columns=['user', 'total_url', 'cheap', 'moderate', 'expensive', 'very expensive'])
files.sort()

for file in files:
    name = file.split('.')[0]
    df = pd.read_csv(path + file)

    Total_URLs = len(df.urls)

    Cheap = len(df[df['category'] == 'Cheap'].urls)
    Moderate = len(df[df['category'] == 'Moderate'].urls)
    Expensive = len(df[df['category'] == 'Expensive'].urls)
    Very_Expensive = len(df[df['category'] == 'Very_Expensive'].urls)

    # print(name, Total_URLs, Cheap, Moderate, Expensive, Very_Expensive, '\n')
    new_row = {'user': name, 'total_url': Total_URLs, 'cheap': Cheap, 'moderate': Moderate, 'expensive': Expensive,
              'very expensive': Very_Expensive}
    dataframe = dataframe.append(new_row, ignore_index=True)

dataframe.to_csv('Data/user_cnt.csv', index=False)
print(dataframe)
