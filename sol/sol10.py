# String Split and Join
# Split the given string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(s):
  s_split = s.split(" ") # split the string into a list of strings
  s_join = "-".join(s_split)

  return s_join

if __name__ == '__main__':
  s = input("enter the string: ")
  result = split_and_join(s)

print(result)