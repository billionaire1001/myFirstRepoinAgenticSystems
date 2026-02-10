def AccessControlSystem(age: int, has_id: bool):
    if age >=18  and has_id:
        print("Entry Allowed")
    else:
        print("Entry Not Allowed")

def parseboolean(value: str) -> bool:
    value = value.strip().lower()
    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        raise ValueError("Verification status must be True/False")

try:
    age = int(input("Age:"))
    has_id_input = input("Has ID(true/false:")
    has_id = parseboolean(has_id_input)
    AccessControlSystem(age, has_id)
except ValueError as e:
    print(f"Invalid input: {e}")