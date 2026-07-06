num = 600851475143
prime_factors = []
divisor = 2
while True:
    if num % divisor == 0:
        if num  == divisor:
            prime_factors.append(divisor)
            break
        num //= divisor
        prime_factors.append(divisor)
        continue
    divisor += 1
print(max(prime_factors))