list1 = [2024,2024,'duplicate','duplicate']

tuple1 = ('unchangable','duplicate','duplicate',222,222)

set1 = {'no duplicates',123,'python'}

dict1 = {"name":"python", "year":2024}
dict2 = {
    "name":"zia",
    "age":28,
    "ocupation":"Doctor"
}

print(list1)
print(tuple1)
print(set1)
print(dict1)
print(dict2)

print(*list1)

for key in dict1.keys():
    print(key,dict1[key])
