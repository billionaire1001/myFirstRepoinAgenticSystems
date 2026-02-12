def password_retry_system() -> None: 
    while True:
        password = input("Enter the correct password:")
        if password == "admin123":
            print("Access Granted")
            break
        
password_retry_system()