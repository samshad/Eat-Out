import pandas as pd


a = False

if not a:
    print('paisi')


'''df1 = pd.read_csv('Saved Datas//All_Restaurant_Data.csv')

title_dict = {}
arr = []

for index, row in df2.iterrows():
    title_dict[row['urls']] = row['titles']

for index, row in df1.iterrows():
    arr.append([title_dict[row['urls'].strip()], row['category'], row['rating'], row['urls'].strip()])

print(len(arr))

df = pd.DataFrame(arr, columns=['title', 'category', 'rating', 'url'])
df.to_csv('Saved Datas/All_Restaurant_Data.csv', index=False)
print('Done...')'''