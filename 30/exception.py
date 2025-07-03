
s = input().strip()

try:
  int_value = int(s)
  print(int_value)
except ValueError:
  print('bad string')