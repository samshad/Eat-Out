from random import choice
import pandas as pd
import requests
from bs4 import BeautifulSoup
import lxml


proxies = []
req = 0


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
    global req
    while 1:
        proxy_string = choice(proxies)
        proxy_dict = {"http": proxy_string, "https": proxy_string}
        try:
            req += 1
            response = requests.get(url, headers=get_agent(), proxies=proxy_dict)
            break
        except:
            pass

    return response


make_proxy_list()


def get_foursq_from_swarmapp(url):
    res = make_request(url)
    print(res.status_code)
    while res.status_code != 200:
        print(res.status_code + ' [swarm]---> ' + url)
        if res.status_code == 404 or res.status_code == 405:
            return
        else:
            res = make_request(url)

    src = res.content
    soup = BeautifulSoup(src, 'lxml')
    new_url = ''

    mydivs = soup.findAll('a')
    for i in mydivs:
        if 'foursquare.com/v/' in i.attrs['href']:
            new_url = i.attrs['href']

    print(new_url)
    if 'foursquare.com/v/' in new_url:
        return new_url
    else:
        return 'https://foursquare.com/v/vecino-del-mar/4dcf2fcaae603b786d43a93e'


def get_url_from_4sq(url):
    res = make_request(url)
    while res.status_code != 200:
        print(res.status_code + ' [4sq]---> ' + url)
        if res.status_code == 404 or res.status_code == 405:
            return
        else:
            res = make_request(url)

    return res.url


def check_if_restaurant(res):
    src = res.content
    soup = BeautifulSoup(src, 'lxml')

    mydivs = soup.find("div", {"class": "categories"})
    if mydivs != None:
        price = mydivs.find("span", {"class": "price"})
        if price != None:
            return True

    return False


def get_restaurant_data(res):
    title = ''
    category = ''
    rating_value = ''
    src = res.content
    soup = BeautifulSoup(src, 'lxml')

    mydivs = soup.find("div", {"class": "categories"})
    if mydivs != None:
        price = mydivs.find("span", {"class": "price"})
        if price != None:
            print(price.attrs['title'])
            category = price.attrs['title']
            ratedivs = soup.find("div", {"class": "venueRateBlock"})
            if ratedivs != None:
                x = ratedivs.find("span", {"class": "venueScore"})
                if x != None:
                    rating = x.find("span", {"itemprop": "ratingValue"})
                    print(rating.text)
                    rating_value = rating.text
            t = soup.find("h1", {"class": "venueName"})
            if t != None:
                title = t.text

    return [title, category, rating_value]

