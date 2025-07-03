mydict = {}
n = int(input())
for i in range(n):
  name,age = input().split()
  mydict[name] = age

print(name)
print(age)
print(mydict)