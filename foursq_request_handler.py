from random import choice
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml


proxies = []


def get_agent():
    agents = ['Branch Metrics API', 'Branch API']
    return {"User-Agent": choice(agents)}


def make_proxy_list():
    df = pd.read_csv('Proxy/proxies.csv')
    plist = list(df.proxies)
    for i in plist:
        a = i.split(':')
        proxies.append('http://' + a[2] + ':' + a[3] + '@' + a[0] + ':' + a[1])


def make_request(url):
    while 1:
        proxy_string = choice(proxies)
        proxy_dict = {"http": proxy_string, "https": proxy_string}
        try:
            response = requests.get(url, headers=get_agent(), proxies=proxy_dict)
            break
        except:
            pass

    return response


make_proxy_list()


def get_foursq_from_swarmapp(url):
    res = make_request(url)
    while res.status_code != 200:
        #print(res.status_code + ' ---> ' + url)
        if res.status_code == 404 or res.status_code == 405:
            return
        else:
            res = make_request(url)

    src = res.content
    soup = BeautifulSoup(src, 'lxml')

    mydivs = soup.findAll('a')
    for i in mydivs:
        if 'foursquare.com/v/' in i.attrs['href']:
            return i.attrs['href']
