#! /usr/bin/env python3

import re
import os
from PIL import Image

for tif in os.listdir("../supplier-data/images/"):
	try:
		img = Image.open("../supplier-data/images/"+tif)
		print(tif," :",img.format,img.size)
		img.resize((600,400)).convert('RGB').save("../supplier-data/images/"+str(re.search(r'\d+', tif).group())+".jpeg","JPEG")
	except OSError:
		pass
