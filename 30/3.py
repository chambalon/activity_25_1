import math


def sol(mealCost,tipPerc,taxPerc):
  tip = (tipPerc/100)*mealCost
  tax = (taxPerc/100)*mealCost
  total = round(mealCost+tip+tax)
  print(total)

if __name__=='__main__':
  mealCost = float(input().strip())
  tipPerc = int(input().strip())
  taxPerc = int(input().strip())

  sol(mealCost,tipPerc,taxPerc)