#! /usr/bin/env python3
import os
import requests

url = "http://localhost/upload/"
for jpg_image in os.listdir("../supplier-data/images/"):
	if ".jpeg" in jpg_image:
		with open('../supplier-data/images/'+jpg_image,'rb') as opened:
			r = requests.post(url, files={'file': opened})
