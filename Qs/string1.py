# changing a string 
# 1- convert the string to a list and then change the value
# 2- using slicing operator


  

if __name__ == '__main__':
  str = "abcdef"

  str_list = list(str)
  str_list[5] = 'z'
  print("".join(str_list))

  # slice the string and join it back
  str = str[:4]+"z"+str[5:]
  print(str)
  