
if __name__ == '__main__':
  n = int(input().strip())
  for i in range(1,11):
    result = n*i
    #print(str(n)+" X "+str(i)+" = "+str(result))
    #print("{} X {} = {}".format(n,i,result))
    print(f'{n} X {i} = {result}')
