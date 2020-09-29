#! /usr/bin/env python3
import os
import requests
import json
import re

url = "http://??/fruits/"
dict_o_dicts = {}

for feed in os.listdir("~/supplier-data/images/"):
        dict_o_dicts[feed] = {}
        with open(("~/supplier-data/images/"+feed), mode='r', encoding='UTF-8') as file:
                dict_o_dicts[feed]["name"] = file.readline().rstrip()
                dict_o_dicts[feed]["weigth"] = int(re.search(r'\d+', file.readline().rstrip()).group())
                dict_o_dicts[feed]["description"] = file.readline().rstrip()
                dict_o_dicts[feed]["image_name"] = file.readline().rstrip()
        response = requests.post(url, data=dict_o_dicts[feed])
        response.raise_for_status()

print(dict_o_dicts)
f = open(filename,'w')
print('whatever', file=f) 