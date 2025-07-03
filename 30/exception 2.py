class Calculator:
  def power(self,n,p):
    if n<0 or p<0 :
      raise Exception("n,p should be non negative")
    else:
      return pow(n,p)
    

cal = Calculator()
t = int(input().strip())
for i in range(t):
  n,p = map(int,input().split())
  try:
    ans = cal.power(n,p)
    print(ans)
  except Exception as error:
    print("Error!")