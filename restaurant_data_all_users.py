import pandas as pd
import foursq_request_handler as fr
import time
import concurrent.futures


start = time.time()

check_saved_4sq = pd.read_csv('Saved Datas/4sq_foursq.csv')
check_saved_swarm = pd.read_csv('Saved Datas/swarm_foursq.csv')
check_saved_not_restaurant_list = pd.read_csv('Saved Datas/Not_Restaurants.csv')
check_saved_restaurant_list = pd.read_csv('Saved Datas/All_Restaurant_Data.csv')

urls_4sq = {}
urls_swarm = {}
urls_not_rest = []
urls_rest_data = {}

data_arr = []
urls_arr = []

req = 0

fr.make_proxy_list()


def from_swarmapp(url):
    global check_saved_swarm
    global urls_swarm
    global req
    if url in urls_swarm:
        return urls_swarm[url]

    x = check_saved_swarm[check_saved_swarm['swarm'] == url]
    if len(x) > 0:
        return list(x['foursq'])[0]

    req += 1
    new_url = fr.get_foursq_from_swarmapp(url)

    urls_swarm[url] = new_url
    return new_url


def from_4sq(url):
    global check_saved_4sq
    global urls_4sq
    global req
    if url in urls_4sq:
        return urls_4sq[url]

    x = check_saved_4sq[check_saved_4sq['4sq'] == url]
    if len(x) > 0:
        return list(x['foursq'])[0]

    req += 1
    new_url = fr.get_url_from_4sq(url)
    if 'swarmapp' in new_url:
        new_url = from_swarmapp(new_url)

    urls_4sq[url] = new_url
    return new_url


def go(i):
    global req
    global urls_not_rest
    global urls_rest_data
    global data_arr
    global check_saved_not_restaurant_list
    global check_saved_restaurant_list

    tweet_id = i[0]
    url = i[1]
    datetime = i[2]
    print(url)

    if '4sq.com' in url:
        url = from_4sq(url)
    elif 'swarmapp.com' in url:
        url = from_swarmapp(url)

    if url in urls_not_rest:
        print('Not Restaurant')
        return

    if url in urls_rest_data:
        a = urls_rest_data[url][0]
        b = urls_rest_data[url][1]
        c = urls_rest_data[url][2]
        d = url
        print('saved dict: ')
        #print([tweet_id, datetime, a, b, c, d])
        data_arr.append([tweet_id, datetime, a, b, c, d])
        return

    x = check_saved_not_restaurant_list[check_saved_not_restaurant_list['urls'] == url]
    if len(x) > 0:
        print('Not Restaurant')
        return

    x = check_saved_restaurant_list[check_saved_restaurant_list['url'] == url]
    if len(x) > 0:
        a = tweet_id
        b = list(x.title)[0]
        c = list(x.category)[0]
        d = list(x.rating)[0]
        e = list(x.url)[0]
        print('saved file: ')
        #print([a, datetime, b, c, d, e])
        data_arr.append([a, datetime, b, c, d, e])
        return

    req += 1
    res = fr.make_request(url)
    while res.status_code != 200:
        print(res.status_code + ' [main]---> ' + url)
        if res.status_code == 404 or res.status_code == 405:
            break
        else:
            res = fr.make_request(url)

    is_restaurant = fr.check_if_restaurant(res)

    if is_restaurant:
        datas = fr.get_restaurant_data(res)
        a = tweet_id
        b = datas[0]
        c = datas[1]
        d = datas[2]
        e = url
        print('Parsed: ')
        print([a, b, c, d, e])
        data_arr.append([a, datetime, b, c, d, e])
        urls_rest_data[url] = [b, c, d]
    else:
        print('rest na: ' + url)
        urls_not_rest.append(url)


def write_files():
    dataframe = pd.DataFrame(data_arr, columns=['tweet_id', 'date', 'title', 'category', 'rating', 'urls'])
    dataframe['date'] = pd.to_datetime(df['date'])
    dataframe.sort_values(by=['date'], inplace=True, ascending=False)
    dataframe.to_csv('Data/Foursq_Data/' + username + '.csv', index=None, header=True)

    not_res = pd.DataFrame(urls_not_rest, columns=['urls'])

    res_arr = []
    for x in urls_rest_data:
        res_arr.append([urls_rest_data[x][0], urls_rest_data[x][1], urls_rest_data[x][2], x])
    res = pd.DataFrame(res_arr, columns=['title', 'category', 'rating', 'urls'])

    foursq_arr = []
    for x in urls_4sq:
        foursq_arr.append([x, urls_4sq[x]])

    foursq_df = pd.DataFrame(foursq_arr, columns=['4sq', 'foursq'])

    swarm_arr = []
    for x in urls_swarm:
        swarm_arr.append([x, urls_swarm[x]])

    swarm_df = pd.DataFrame(swarm_arr, columns=['swarm', 'foursq'])

    not_res.to_csv('Saved Datas/Not_Restaurants.csv', index=False, header=False, mode='a')
    res.to_csv('Saved Datas/All_Restaurant_Data.csv', index=False, header=False, mode='a')
    foursq_df.to_csv('Saved Datas/4sq_foursq.csv', index=False, header=False, mode='a')
    swarm_df.to_csv('Saved Datas/swarm_foursq.csv', index=False, header=False, mode='a')

    urls_4sq.clear()
    urls_rest_data.clear()
    urls_swarm.clear()


def global_init():
    global check_saved_4sq
    global check_saved_swarm
    global check_saved_not_restaurant_list
    global check_saved_restaurant_list
    check_saved_4sq = pd.read_csv('Saved Datas/4sq_foursq.csv')
    check_saved_swarm = pd.read_csv('Saved Datas/swarm_foursq.csv')
    check_saved_not_restaurant_list = pd.read_csv('Saved Datas/Not_Restaurants.csv')
    check_saved_restaurant_list = pd.read_csv('Saved Datas/All_Restaurant_Data.csv')

    global urls_4sq
    global urls_swarm
    global urls_not_rest
    global urls_rest_data
    urls_not_rest = []
    urls_4sq.clear()
    urls_rest_data.clear()
    urls_swarm.clear()

    global data_arr
    global urls_arr
    data_arr = []
    urls_arr = []


cnt = 0
un = pd.read_csv('Data/userlist.csv')
users = list(un.users)
users.sort()

for user in users[1:3]:
    global_init()
    cnt += 1
    print('Count: ' + str(cnt) +
          '===================================================================================='
          + '\n====================================================================================')
    username = user
    df = pd.read_csv('Data/Initial URLs/' + username + '.csv')

    for index, row in df.iterrows():
        urls_arr.append([row['id'], row['url'], row['date']])

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        executor.map(go, urls_arr)

    time.sleep(5)
    write_files()

print('Total: ' + str(len(urls_arr)) + '\n' + 'Request: ' + str(req))
print('Not Request: ' + str(len(urls_arr) - req))

hours, rem = divmod(time.time() - start, 3600)
minutes, seconds = divmod(rem, 60)
print("Time Taken: {:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
