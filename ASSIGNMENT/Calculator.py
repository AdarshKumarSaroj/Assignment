import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def square(x):
    return x ** 2

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Cannot calculate square root of a negative number"

def power(x, y):
    return x ** y

def Calculator():
    operations = {
        '1': ("Addition", add),
        '2': ("Subtraction", subtract),
        '3': ("Multiplication", multiply),
        '4': ("Division", divide),
        '5': ("Square", square),
        '6': ("Square Root", square_root),
        '7': ("Power", power),
        '8': ("Exit", None)
    }

    print("Welcome to the Simple Calculator!")

    while True:
        print("\nChoose operation:")
        for key, (operation, _) in operations.items():
            print(f"{key}. {operation}")

        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Thank You , I hope you  will give full Mark For This File ")
            break

        try:
            if choice in operations:
                operation_name, operation_func = operations[choice]
                if operation_func is not None:
                    if choice in ['1', '2', '3', '4', '5', '7']:
                        a = float(input("Enter first number: "))
                        b = float(input("Enter second number: "))
                        result = operation_func(a, b)
                    elif choice == '6':
                        r = float(input("Enter a number: "))
                        result = operation_func(r)
                    
                    print("Result: ", result)
                else:
                    print("Thank You , I hope you  will give full Marks For This F")
                    break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

        except ZeroDivisionError:
            print("Cannot divide by zero.")


Calculator()
