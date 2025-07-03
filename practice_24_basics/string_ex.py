mystring = 'sunset'

print(mystring,"\n")

for char in mystring:
    print(char)

print("length of string is",len(mystring))
indx =0
while indx < len(mystring):
    print(mystring[indx])
    indx+=1

print("****************************")
print(mystring[0])
print(mystring[2])

print(mystring.splitlines())
print(mystring.split())

copied_string = mystring[:]
print("copied string: ",copied_string)
