# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

import hashlib

if __name__ == '__main__':
  n = int(input("Enter n: "))
  t = tuple(map(int,input("enter "+ str(n)+ " integers: ").split()))

print(t)
print(hash(t))