#! /usr/bin/env python3
import os
import requests
import json
import re

url = "http://34.122.175.55/fruits/"
dict_o_dicts = {}

for feed in os.listdir("../supplier-data/descriptions/"):
	dict_o_dicts[feed] = {}
	img_num = 0
	with open(("../supplier-data/descriptions/"+feed), mode='r', encoding='UTF-8') as file:
		dict_o_dicts[feed]["name"] = file.readline().rstrip()
		dict_o_dicts[feed]["weight"] = int(re.search(r'\d+', file.readline().rstrip()).group())
		dict_o_dicts[feed]["description"] = file.readline().rstrip()
		img_num += 1
		if img_num < 10:
			dict_o_dicts[feed]["image_name"] = "00"+str(int(re.search(r'\d+', feed).group()))+".jpeg"
		else:
			dict_o_dicts[feed]["image_name"] = "0"+str(int(re.search(r'\d+', feed).group()))+".jpeg"
	print(dict_o_dicts[feed])
	response = requests.post(url, data=dict_o_dicts[feed])
	response.raise_for_status()

with open('../dict_o_dicts.json', 'w') as outfile:
    json.dump(dict_o_dicts, outfile)