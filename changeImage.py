#! /usr/bin/env python3

import os
from PIL import Image

for tif in os.listdir("~/supplier-data/images/"):
	try:
		img = Image.open(tif)
		print(img.format,img.size)
		img.resize((600,400)).convert('RGB').save("~/supplier-data/images/"+tif+".jpeg","JPEG")
	except OSError:
		pass
