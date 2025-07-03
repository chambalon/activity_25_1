# Print all even numbers between 1 to 10

def evenNum():
    for n in range(1,11):
        while n%2 == 0:
            print(str(n))
            break
print("Even numbers:")
evenNum()