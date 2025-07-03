# find two indices in an array where the numbers add up to a given target using a hashmap
def two_sum(nums, target):
  num_map = {}
  for i, num in enumerate(nums):
    complement = target - num
    if complement in num_map:
      return [num_map[complement],i]
    num_map[num] = i
  return None

nums = [4,7,1,2]
target = 3

result = two_sum(nums,target)
print(result)