def is_prime(number):
    if number<2:
        return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True
primes=[]
def prime_list(n):
    for i in range(n+1):
        if is_prime(i):
            primes.append(i)
    return primes
t=int(input("enter a number:"))
print(prime_list(t))


