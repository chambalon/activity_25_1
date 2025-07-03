test_score = int (input("Enter your score:"))

while test_score < 0 or test_score > 100:
    print("Invalid score! Enter a score between 0 and 100")
    test_score = int (input("Enter your score:"))
    break
    