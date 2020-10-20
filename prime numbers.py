def is_prime(prime_number):
    if prime_number > 1:
        for numbers in range(2, prime_number):
            if prime_number % numbers == 0:
                return False
        return True


print(is_prime(6857))