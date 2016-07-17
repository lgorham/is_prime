def is_prime(num):
    """Takes a number and returns True if prime, and False if not prime"""

    if num <= 1:
        return False
    else:
        for i in range(2, (int(num**0.5)+1)):
            if num % i == 0:
                return False
        return True

print is_prime(-10)