# in and not in -> returns boolean. syntax: element in /not in listname
# in or not in - list
mylist= [11,22,33,44,"abc"]
print(33 in mylist)
print(33 not in mylist)
print("abc" in mylist)
print(1000 in mylist)

# in or not in - tuple
t1= (1,2,3)
print("is 2 in t2:", 2 in t1)
       
print("***************************************")

# in or not in - dictionary ; use if/ else and check with keys not value
dict1={'Western Australia':'Perth',
       'New south Wales':'Sydney',
       'Soth Australia':'Adelaide',
       'Queensland':'Brisbane'
       }

if 'Soth Australia' in dict1:
    print("Present")
else:
    print("not present")

if 'Sydney' in dict1:
    print("Present")
else:
    print("not present")
print("***************************************")

# method2 -to check keys
for key in dict1.keys():
    if key in dict1:
        print(key, "present")
    else:
        print(key, "present")
print("***************************************")
# method2 -to check values
for key in dict1.keys():
    if key in dict1:
        print(dict1[key], "present")
    else:
        print(dict1[key], "present")


    