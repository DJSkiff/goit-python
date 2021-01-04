def is_prime(n, d=3):
    while d > 1:
        if n % d == 0:
            return False
        else:
            return is_prime(n, d - 1)
    return True


print(is_prime(1999))
