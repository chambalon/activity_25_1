from collections import Counter
import heapq

def topKFreq(nums,k):
  frequency = Counter(nums)
  min_heap = []

  for num, fq in enumerate(frequency.items()):
    heapq.heappush(min_heap, (fq,num))
    if len(min_heap)>k:
      heapq.heappop(min_heap)
  return [num for fq, num in min_heap]


nums = [1,1,1,2,2,3]
k = 2
print(topKFreq(nums,k))