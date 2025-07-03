# Read a given CSV file as a list

import csv

with open('record1.csv', newline='') as csvfile:
  data = csv.reader(csvfile)   # read csvfile with default delimeter ','
  data_list = list(data)
  print(data_list)