from collections import deque


class Solution():
  def __init__(self):
    #self.stack = []
    #self.queue = []
    self.stack = deque()
    self.queue = deque()

  def pushCharacter(self,character):
    self.stack.append(character)
  def enqueueCharacter(self,character):
    self.queue.append(character)
  def popCharacter(self):
    return self.queue.pop()
  def dequeueCharacter(self):
    #return self.queue.pop(0)
    return self.queue.popleft()



s = input()
l = len(s)

obj = Solution()

for i in range(l):
  obj.pushCharacter(s[i])
  obj.enqueueCharacter(s[i])


isPalindrome = True

for j in range(l//2):
  if obj.popCharacter() != obj.dequeueCharacter():
    isPalindrome = False
    break
if isPalindrome:
  print(f'{s} is palindrome')
else:
  print(f'{s} is not a palindrome')



