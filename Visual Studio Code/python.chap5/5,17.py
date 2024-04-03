def is_prime(n, primes):
    for prime in primes:
        if n % prime == 0:
            return False
        if prime * prime > n:
            break
    return True

def generate_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i, primes):
            primes.append(i)
    return primes

n = 100 
primes = generate_primes(n)
print(primes)

