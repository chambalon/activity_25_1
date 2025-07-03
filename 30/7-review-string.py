
def myfunc(s):
  str_even_indexed = ""
  str_odd_indexed = ""
  for j in range(0,len(s)):
    if j%2 == 0:
      str_even_indexed += s[j]
    elif j%2 == 1:
      str_odd_indexed += s[j]

 # print(str_even_indexed + " "+ str_odd_indexed)
  print('{} {}'.format(str_even_indexed,str_odd_indexed))



if __name__ == '__main__':
  testCases = int(input().strip())
  for i in range(0,testCases):
    s = input().strip()
    x = myfunc(s)
    