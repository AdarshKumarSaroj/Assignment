







def sum_of_even_natural_numbers(N):
    if N < 1:
        return "Please enter a positive integer for N."
    
    sum_even = N * (N + 1)
    return sum_even


N = int(input("Enter : "))
result = sum_of_even_natural_numbers(N)
print(f"Sum of the first {N} even natural numbers: {result}")

def sum_of_odd_natural_numbers(N):
    if N < 1:
        return "Please enter a positive integer for N."
    
    sum_odd = N ** 2
    return sum_odd


N = int(input("Enter : "))
result = sum_of_odd_natural_numbers(N)
print(f"Sum of the first {N} odd natural numbers: {result}")
