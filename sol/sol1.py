if __name__ == '__main__':


  n =int(input("enter an integer between 1 and 100:").strip())

if n%2!=0:
  print("weird")
elif n%2==0 and n in range(2,6):
  print("not weird")
elif n%2==0 and n in range(6,21):
  print("weird")
elif n%2==0 and n>20:
  print("not weird")

