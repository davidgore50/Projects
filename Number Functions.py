def largest_prime_factor(n):
    factor = 2
    print(f"Starting with n = {n}")
    while factor * factor <= n:
        if n % factor == 0:
            print(f"{n} is divisible by {factor}, dividing...")
            n //= factor
            print(f"New n = {n}")
        else:
            factor += 1
    print(f"Largest prime factor found: {n}")
    return n

# Example usage
number = 600851475143
largest_prime_factor(number)