#!/usr/bin/env python3
import shutil
import psutil
import os
import emails
import socket
import sys

def check_cpu_usage():
	usage = psutil.cpu_percent(1)
	return usage < 80

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free / du.total * 100
	return free > 20

def check_memory_usage():
    available = psutil.virtual_memory()[1]/2.**20
    return available > 524.288

def main(argv):	
	"""Process the JSON data and generate a full report out of it."""
	print(socket.gethostbyname(socket.gethostname()))
	subject_line = ""
	if not check_cpu_usage() :
		subject_line = "Error - CPU usage is over 80%"
	elif not check_disk_usage("/") :
		subject_line = "Error - Available disk space is less than 20%"
	elif not check_memory_usage() :
		subject_line = "Error - Available memory is less than 500MB"
	#elif not (socket.gethostbyname(socket.gethostname()) == "127.0.0.1"):
	#	subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
	else:
		print("Everything is OK :)")

	if not (subject_line == ""):
		print(subject_line)
		sender = "automation@example.com"
		receiver = "{}@example.com".format(os.environ.get('USER'))
		subject = subject_line
		body = "Please check your system and resolve the issue as soon as possible."

		message = emails.generate2(sender, receiver, subject, body)
		emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
