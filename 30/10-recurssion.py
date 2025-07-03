def fact(n):
  if n<=0:
    return 1
  else:
    return n*fact(n-1)

if __name__ == '__main__':
  n = int(input())
  x = fact(n)
  print(x)