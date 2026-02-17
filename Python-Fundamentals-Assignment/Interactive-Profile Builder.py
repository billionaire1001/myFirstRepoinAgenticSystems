name = input("Enter your name: ")
age = input("Enter your age: ")
active = input("Are you an active user? (True / False): ")
active_status = active.strip().lower() == "true"
print(f"User {name.title()} is {age} years old. Active status: {active_status}")