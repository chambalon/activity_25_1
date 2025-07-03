# 1. Read each row from a given csv file and print a list of strings 
'''
Note:
delimiter: A one-character string used to separate fields. It defaults to ','.
quotechar: The quotechar optional parameter tells the writer which character to use to quote fields when writing.
'''

import csv

with open('record1.csv', newline='') as csvfile:
  data = csv.reader(csvfile, delimiter=',',quotechar='|')   # read csvfile with default delimeter ','
  for row in data:
    print(','.join(row))    # join row elements with comma
    # print(' '.join(row))  # join row elements with space
  
  