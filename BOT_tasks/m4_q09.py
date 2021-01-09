def is_prime(n, d=3):
    if n == 1:
        return False
    elif n % d == 0:
        return False
    else:
        return is_prime(n, d+1) if d * d <= n else True


print(is_prime(1999))
