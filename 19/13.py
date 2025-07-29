def solution(str):
  def expand_around_centers(left,right):
    while left>=0 and right<len(str) and str[left] == str[right]:
      left -= 1
      right += 1
    return str[left+1:right]

  result = ""
  for i in range(len(str)):
    result = max(result, expand_around_centers(i,i), expand_around_centers(i,i+1), key=len)
  return result
  

print(solution('babad'))
print(solution('babba'))
