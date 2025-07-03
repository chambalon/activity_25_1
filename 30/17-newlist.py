# Write a Function to Return a New List Where All None Values Are Replaced with the Most Recent Non-None Value in the List.
def solution(list1):
  newList = []

  prevValue = None
  for e in list1:
    if e is None:
      newList.append(prevValue)
    else:
      newList.append(e)
      prevValue = e
  
  return newList



list1 = [2,None,4,7,None,3]
op = solution(list1)
print(op)