#!/usr/bin/env python3

import json
import locale
import sys
import operator
import emails
import os
import reports
import time
import datetime

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, report_info])

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data

def process_data(data):
  '''
  Takes the json dictionary and turns it into a string list
  that is rady and available to process into the report.
  Like : "name: *Fruit name*
          weigth: *Fruit weigth* lbs"
  '''
  #data_list = []
  data_string = ""
  for value in data.values():
    data_string += "<br/>" + "<br/>" + "name: " + value["name"] + \
      "<br/>" + "weigth: " + str(value["weigth"]) + " lbs"
    #data_list.append(data_string)
  return data_string

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("../dict_o_dicts.json")
  processed = process_data(data)  
  print(processed)

  titulo = "Processed Update on " + datetime.date.today().strftime("%B %d, %Y") # Add the date in international format
  # Like: March 11, 2020

  reports.generate("../processed.pdf", 
    titulo, processed)

  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate(sender, receiver, subject, body,"../processed.pdf")
  #emails.send(message)

if __name__ == "__main__":
  main(sys.argv)