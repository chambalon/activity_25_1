# find the contiguous subarray with the largest sum using kadane's algorithm

def max_subarray_sum(nums):
  max_sum = float('-inf')
  current_sum = 0
  start_index = 0
  end_index = 0
  j =0

  for i in range(len(nums)):
    current_sum += nums[i]

    if current_sum > max_sum:
      max_sum = current_sum
      start_index = j
      end_index = i

    if current_sum < 0:
      current_sum = 0
      j = i+1

  return max_sum, nums[start_index:end_index+1]

nums = [-2,-3,4,-1,-2,1,5,-3]

max_sum, max_subarray = max_subarray_sum(nums)
print(f'maximum sum: {max_sum}')
print(f'subarray: {max_subarray}')