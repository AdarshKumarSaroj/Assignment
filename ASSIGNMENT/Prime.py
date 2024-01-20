def Prime_Generater(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            # print(num)
            return False
    # print(num)
    return True

def generate_primes(limit):
    primes = []
    for num in range(2, limit):
        if Prime_Generater(num):
            # print(num)
            primes.append(num)
    return primes


limit = 50
prime_numbers = generate_primes(limit)
print(f"Prime numbers up to {limit}: {prime_numbers}")

