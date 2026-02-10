def SecureTransactionValidator(Balance: int, Withdrawal: int, Verified : bool):
    if Verified and Withdrawal <= Balance:
        print("Withdrawal Successful")
    else:
        print("Transaction Denied")


def parseBoolean(value: str) -> bool:
    value = value.strip().lower()
    if value == "true":
        return True
    elif value == "false":
        return False
    else:
        raise ValueError("Verification status must be True/False")


try:
    Balance = int(input("Account Balance: "))
    Withdrawal = int(input("Withdrawal Amount: "))
    Verified_input = input("Verification Status (True/False): ")
    Verified = parseBoolean(Verified_input)

    SecureTransactionValidator(Balance, Withdrawal, Verified)

except ValueError as e:
    print(f"Invalid input: {e}")