# Read a given CSV file as a dictionary

import csv

'''
with open('record1.csv', newline='') as csvfile:
  dict_data = csv.DictReader(csvfile)  
  for row in dict_data:
    print(row) 

'''

dict_data = csv.DictReader(open('record1.csv'))
for row in dict_data:
    print(row) 

