#! /usr/bin/env python3
import os
import requests
import json
import re

url = "http://35.222.198.14/fruits/"
dict_o_dicts = {}

for feed in os.listdir("../supplier-data/descriptions/"):
        dict_o_dicts[feed] = {}
        img_num = 1
        with open(("../supplier-data/descriptions/"+feed), mode='r', encoding='UTF-8') as file:
                dict_o_dicts[feed]["name"] = file.readline().rstrip()
                dict_o_dicts[feed]["weigth"] = int(re.search(r'\d+', file.readline().rstrip()).group())
                dict_o_dicts[feed]["description"] = file.readline().rstrip()
                if img_num < 10:
                        dict_o_dicts[feed]["image_name"] = "0"+str(img_num)+".jpeg"
                else:
                	dict_o_dicts[feed]["image_name"] = "00"+str(img_num)+".jpeg"
        response = requests.post(url, data=dict_o_dicts[feed])
        response.raise_for_status()

with open('../dict_o_dicts.json', 'w') as outfile:
    json.dump(dict_o_dicts, outfile)