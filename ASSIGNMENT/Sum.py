def sum_numbers():
    print("Press Ctrl + C to provide all data or Press enter for sum")
    storage = []
    count = 1

    try:
        while True:
            inp = int(input(f"\nEnter your {count} number: "))
            count += 1
            storage.append(inp)

    except:
        print("\n ----->     Sum of all entered numbers:", sum(storage))

if __name__ == "__main__":
    sum_numbers()





