# take inputs in a single line and add to the list
n = int(input("n: "))
alist = list(map(int, input("enter "+ str(n) + " numbers: ").split()))
print(alist)

# take inputs in multiple lines and add those in a list
alist = []
for i in range(int(input("n: "))):
  elements = int(input("element: "))
  alist.append(elements)
print(alist)