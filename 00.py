import pandas as pd
import os
import json
import foursq_request_handler as fr


df = pd.read_csv('Sample Datas/Initial URLs/ThisIsTee1.csv')
check_4sq = pd.read_csv('Saved Datas/4sq_foursq.csv')
check_4sq = pd.read_csv('Saved Datas/4sq_foursq.csv')
check_saved_not_restaurant_list = pd.read_csv('Saved Datas/Not_Restaurants.csv')
check_saved_restaurant_list = pd.read_csv('Saved Datas/All_Restaurant_Data.csv')
print(check_saved_restaurant_list)

#fr.make_proxy_list()

