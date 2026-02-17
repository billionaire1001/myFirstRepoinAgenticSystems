def check_even_or_odd(number):
    if number % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"


if __name__ == "__main__":
    result = check_even_or_odd(4)
    print(result)