#!/usr/bin/env python3
import shutil
import psutil

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 80

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def check_memory_usage():
    available = psutil.virtual_memory()[1]/2.**20
    return available > 500

if not check_cpu_usage() 
    or not check_disk_usage("/") 
    or not check_memory_usage():
	print("ERROR !")	
else:
	print("Everything is OK :)")

