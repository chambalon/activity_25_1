# Product of Array Except Self
"""
Given an array of numbers, 
the goal is to create a new array where each element at index i 
is the product of all the numbers in the original array except the number at index i.
"""

def product_except_self(nums):
  n= len(nums)
  nums2 = [1] * n

  left = 1
  for i in range(n):
    nums2[i] = left
    left *= nums[i]

  right = 1
  for i in range(n-1,-1,-1):
    nums2[i] *= right
    right *= nums[i]

  return nums2

nums = [2,3,4,5]

result = product_except_self(nums)
print(result)
