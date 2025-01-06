#Task 1
def add():
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    return num_1 + num_2

def sub():
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    return num_1 - num_2

def mul():
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    return num_1 * num_2

def div():
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    return num_1 / num_2



def main():
    while True:
        try:
            operator = input("How would you like to calculate your numbers (+, -, *, /)? ")

            if operator == "+":
                print(add())
            elif operator == "-":
                print(sub())
            elif operator == "*":
                print(mul())
            elif operator == "/":
                print(div())
            else:
                print("Unknown operation. Please choose again")
        except ZeroDivisionError:
            print("Error")

if __name__ == "__main__":
    main()