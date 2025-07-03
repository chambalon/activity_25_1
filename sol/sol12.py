# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(s,i,c):
  s = s[:i]+ c + s[i+1:]
  return s

  '''
  s = list(s)
  s[i] = c
  return "".join(s)

  '''

if __name__ == '__main__':
  s = input("Enter the string: ")
  i = int(input("Enter the index: "))
  c = input("Enter the character: ")
  result = mutate_string(s,i,c)
  print(result)
