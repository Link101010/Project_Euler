def prime_factors(num):
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
    return prime_factors

divisors = []
for i in range(2,21):
    temp_prime_factors = prime_factors(i)
    for factor in set(temp_prime_factors):
        if factor not in divisors:
            divisors.append(factor)
        elif temp_prime_factors.count(factor) > divisors.count(factor):
            for i in range(temp_prime_factors.count(factor) - divisors.count(factor)):
                divisors.append(factor)

product = 1
for i in divisors:
    product *= i
print(product)