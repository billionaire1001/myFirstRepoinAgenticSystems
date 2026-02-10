def passOrFailChecker(score: int):
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
        
try:
    score = int(input("Enter the score:"))
    passOrFailChecker(score)
except ValueError:
    print("Invalid score! Please enter a valid integer score.")

