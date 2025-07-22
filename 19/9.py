def permute(nums):
  result = []  
  n = len(nums)
    
  def backtrack(current_permutation, available_nums): 
    if len(current_permutation) == n:
      result.append(current_permutation) 
      return
    
    for i in range(len(available_nums)):
      backtrack(current_permutation + [available_nums[i]] , available_nums[:i] + available_nums[i+1:] )

  backtrack([], nums)
  return result

nums = [1,2,3]
p = permute(nums)
print(p)

