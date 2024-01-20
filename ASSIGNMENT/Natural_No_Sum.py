def sum_of_natural_numbers(n):
    if n < 1:
        return "Please enter a positive integer."


    return n * (n + 1) // 2

def main():
    try:
        n = int(input("Enter a positive integer: "))
        result = sum_of_natural_numbers(n)
        print(f"The sum of natural numbers Between {n} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")


main()
