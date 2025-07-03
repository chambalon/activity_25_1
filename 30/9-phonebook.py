import sys

if __name__ == '__main__':
  no_of_entries = int(sys.stdin.readline().strip())
  phoneBook = dict()

  for i in range(no_of_entries):
    entry_list = sys.stdin.readline().strip().split()
    phoneBook[entry_list[0]] = entry_list[1]
  print(phoneBook)


  query = sys.stdin.readline().strip()
  while query:
    phone_number = phoneBook[query]   # or phoneBook.get(query)
      
    if phone_number:
      print(f'{query} = {phone_number}')
    else:
      print("Not Found")
    break
    #query = sys.stdin.readline().strip()
    
    
    