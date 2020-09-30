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

def generate(filename, title):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph("additional_info", styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line])

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data

def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("../dict_o_dicts.json")
  #print(data)
  # TODO: turn this into a PDF report

  titulo = "Processed Update on " + datetime.date.today().strftime("%B %d, %Y") # Add the date in international format
  # Like: March 11, 2020

  reports.generate("../tmp/processed.pdf", 
    titulo)

  sender = "sender@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  #body = data

  message = emails.generate(sender, receiver, subject, "body","../tmp/processed.pdf")
  #emails.send(message)
  # TODO: send the PDF report as an email attachment


if __name__ == "__main__":
  main(sys.argv)