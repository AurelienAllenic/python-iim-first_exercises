def fizzbuzz():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        raise ValueError("That's not a number!")
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return number

print(fizzbuzz())
