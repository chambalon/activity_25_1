# swap cases. Convert all lowercase letters to uppercase letters and vice versa.

def swapCase(s):
  str = ""
  for i in s:
    if i.isupper() == True:
      str+=i.lower()
    else:
      str+=i.upper()
  return str


if __name__ == '__main__':

  s = input("enter the sentence: ")

  #s1 = input("enter the sentence: ").split()
  #s = " ".join(s1)
  

  print(s)

  output = swapCase(s)
 
#print(s)
#print(" ".join(s))

print(output)