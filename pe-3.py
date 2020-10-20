def largest_prime_factor(prime_factor):
    number = 2
    while number * number < prime_factor:
        while prime_factor % number == 0:
            prime_factor = prime_factor / number
        number = number + 1
    return prime_factor


print(largest_prime_factor(600851475143))