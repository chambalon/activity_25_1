def solution(str):
  if len(str)%2 != 0:
    return False
  stack, mapping = [], {')':'(','}':'{',']':'['}
  for char in str:
    if char in mapping:
      if stack and stack[-1] == mapping[char]:
        stack.pop()
      else:
        return False
    else:
      stack.append(char)
  
  return not stack
   

print(solution('()[]{}'))
print(solution('{]'))
print(solution('([])'))
print(solution('[]{'))
