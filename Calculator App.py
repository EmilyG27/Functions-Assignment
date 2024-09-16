#Task 1

while True:
    try:
        number_1 = float(input("What is the first number?: "))
        number_2 = float(input("What is the second number?: "))
        operator = input("How would you like to calculate your numbers (+, -, *, /)? ")

        if operator == "+":
            print(number_1 + number_2)
        elif operator == "-":
            print(number_1 - number_2)
        elif operator == "*":
            print(number_1 * number_2)
        elif operator == "/":
            print(number_1 / number_2)
        else:
            print("Unknown operation. Please choose again")
    except ZeroDivisionError:
        print("Error")