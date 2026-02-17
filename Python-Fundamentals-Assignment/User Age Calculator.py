from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter your birth year: "))
age = calculate_age(birth_year)
if age < 0:
    print("You are not born yet.")
    exit()
print(f"You are {age} years old.")