# Write a Python function that takes a list of numbers and returns a new list containing only the even numbers, 
# using list comprehension

list1 = list(map(int, input().split()))

evenNums = [e for e in list1 if e%2 == 0]

print(evenNums)