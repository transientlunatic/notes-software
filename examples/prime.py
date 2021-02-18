def is_prime(number):
    """Test if a number is prime. Return True if prime, and False if not."""
    if (number == 2):
        return True
    for i in range(2, number):
        if number % 2 == 0:
            return False
        elif (number % i) == 0:
            return False
        else:
            return True
