def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True


def get_smaller_primes(n):
    smaller_primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            smaller_primes.append(num)
    return smaller_primes

print(get_smaller_primes(9))
