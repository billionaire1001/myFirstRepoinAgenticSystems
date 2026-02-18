def main():
    marks = [78, 85, 90, 65, 72, 88, 92, 80]

    first_three = marks[:3]
    last_three = marks[-3:]

    print("First 3 marks:", first_three)
    print("Last 3 marks:", last_three)

    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Average:", average)


if __name__ == "__main__":
    main()