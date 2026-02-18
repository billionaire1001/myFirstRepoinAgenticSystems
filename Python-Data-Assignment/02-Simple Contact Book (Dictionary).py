def main():
    contacts = {
        "Raj": "9450882228",
        "Abhilash": "7388965873",
        "Somnath": "9198218824",
    }

    print("All contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

    search_name = input("Enter a name to search: ")

    if search_name in contacts:
        print(f"Phone number for {search_name}: {contacts[search_name]}")
    else:
        print("Contact not found")


if __name__ == "__main__":
    main()