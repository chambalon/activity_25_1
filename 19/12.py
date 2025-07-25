
def longest_common_prefix(strs):
  if not strs:
    return ""
  for i,char in enumerate(strs[0]):
    for s in strs[1:]:
      if i == len(s) or char != s[i]:
        return strs[0][:i]
  return strs[0]   

print(longest_common_prefix(['raindrops','rain','rainbow']))
print(longest_common_prefix(['flower','flow','flight']))
print(longest_common_prefix(['sky','stars','dusky']))



