'''def permute(nums):
  result = []  
  n = len(nums)
    
  def backtrack(current_permutation, available_nums): 
    if len(current_permutation) == n:
      result.append(list(current_permutation))  
      return
    print("available_nums",available_nums)
    for i in range(len(available_nums)):
      print("available_nums",available_nums)
      print(i)
      num = available_nums[i] 
      current_permutation.append(num)      
      new_available_nums = available_nums[:i] + available_nums[i+1:]  
      print("new available_nums",new_available_nums)

      print("(1)",current_permutation, new_available_nums)
      backtrack(current_permutation, new_available_nums)
      print("(2)",current_permutation, new_available_nums)
      current_permutation.pop()
      print("(3)",current_permutation, new_available_nums)


  backtrack([], nums)
  return result

nums = [1,2,3]
p = permute(nums)
print(p)

'''