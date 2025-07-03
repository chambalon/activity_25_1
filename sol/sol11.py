#
def printfunc(firstname,lastname):
  # return print(f'Hello {firstname} {lastname}! Welcome')
  # return print('Hello {} {}! Welcome'.format(firstname,lastname))
  # return print("Hello", firstname, lastname,"! Welcome")
  return print("Hello "+firstname + " " +lastname+"! Welcome")
        
if __name__ == '__main__':
  firstname = input("firstname: ")
  lastname = input("lastname: ")

  op = printfunc(firstname,lastname)