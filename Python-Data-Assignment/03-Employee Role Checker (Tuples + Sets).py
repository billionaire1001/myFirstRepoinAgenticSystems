def main():
    employee = (101, "Abhilash", "IT")

    roles = {"editor", "viewer", "admin"} 

    print("Employee Information:")
    print("ID:", employee[0])
    print("Name:", employee[1])
    print("Department:", employee[2])

    has_admin = "admin" in roles

    print("Admin Access:", "Yes" if has_admin else "No")


if __name__ == "__main__":
    main()