import pandas as pd
import os
import json
import foursq_request_handler as fr


df = pd.read_csv('Sample Datas/Initial URLs/ThisIsTee1.csv')
#print(df)

fr.make_proxy_list()
#res = fr.make_request('https://foursquare.com/v/t-spesjalleke/4c94ec0d533aa09384d5c345')
res = fr.get_foursq_from_swarmapp('https://www.swarmapp.com/c/3p7eA7RBcIN')
print(res)
#print(res.status_code)
#print(res.content)
