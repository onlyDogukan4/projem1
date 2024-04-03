u = int(input('Enter first number: '))
v = int(input('Enter second number: '))
smallest = min(u, v)
gcd = 1

for d in range(2, smallest + 1):
    while u % d == 0 and v % d == 0:
        gcd *= d
        u //= d
        v //= d

print('The gcd is', gcd)