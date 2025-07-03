# dictionaries are case sensitive

dict1={'Western Australia':'Perth',
       'New South Wales':'Sydney',
       'South Australia':'Adelaide',
       'Queensland':'Brisbane'
       }

print(dict1)
print(dict1["Queensland"])
print("*****************************")
for key in dict1.keys():
    print(key, dict1[key])

print("*****************************")
# updating 
dict1['Victoria']= 'Melbourne'
print(dict1)
dict1['Victoria']= 'updated'
print(dict1)

print("***************************************")

# dict.get()
print(dict1.get('Queensland'))
#print(dict1.get('Sydney'))
#print(dict1.get(dict1["Queensland"]))
print(dict1.get('India'))
print(dict1.get('India','It\'s far away'))

print("*****************************")
# in not in
if 'Soth Australia' in dict1:
    print("Present")
else:
    print("not present")

# method2
for key in dict1.keys():
    if key in dict1:
        print(key, "present")
    else:
        print(key, "present")
if 'Sydney' in dict1:
    print("Present")
else:
    print("not present")
print("***************************************")

for key in dict1.keys():
    if key in dict1:
        print(dict1[key], "present")
    else:
        print(dict1[key], "present")
print("***************************************")
# remove
# del - doesnt return any value
del dict1['Victoria']
# pop - returns value of the key removed
print(dict1.pop('South Australia'))
print(dict1)

        
        


    
