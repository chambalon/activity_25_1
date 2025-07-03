# Read a given CSV file having tab delimiter

import csv

with open('record2.csv',newline='') as csvfile:
  data = csv.reader(csvfile,delimiter='\t')     # read csvfile with default delimeter 'tab'
  for row in data:
    print(' '.join(row))    