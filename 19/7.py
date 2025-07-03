# Trapping Rain Water
# Compute how much water can be trapped between each bars and input the total water

def trapping_water(heights):
  left,right = 0,len(heights)-1
  water = 0
  left_max = right_max = 0
  
  while left < right:
    if heights[left] < heights[right]:
      left_max = max(left_max, heights[left])
      water += left_max - heights[left]
      left +=1
    else:
      right_max = max(right_max, heights[right])
      water += right_max - heights[right]
      right -= 1

  return water


heights = [0,1,0,2,1,0,1,3,2,1,2,1]
water = trapping_water(heights)
print(water)