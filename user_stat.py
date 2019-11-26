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

    Cheap = round(len(df[df['category'] == 'Cheap'].urls)/Total_URLs, 2)
    Moderate = round(len(df[df['category'] == 'Moderate'].urls)/Total_URLs, 2)
    Expensive = round(len(df[df['category'] == 'Expensive'].urls)/Total_URLs, 2)
    Very_Expensive = round(len(df[df['category'] == 'Very_Expensive'].urls)/Total_URLs, 2)

    # print(name, Total_URLs, Cheap, Moderate, Expensive, Very_Expensive, '\n')
    new_row = {'user': name, 'total_url': Total_URLs, 'cheap': Cheap, 'moderate': Moderate, 'expensive': Expensive,
              'very expensive': Very_Expensive}
    dataframe = dataframe.append(new_row, ignore_index=True)

dataframe.to_csv('Data/user_stat.csv', index=False)
print(dataframe)
