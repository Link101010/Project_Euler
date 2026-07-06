import math

def is_prime(num):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

primes = []
for i in range(2,2000000):
    primes.append(i) if is_prime(i) else None
print(sum(primes))