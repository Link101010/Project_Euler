import math

def is_prime(num):
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

count = 0
divisor = 2
while count != 10001:
    if is_prime(divisor):
        count += 1
        divisor += 1
    else:
        divisor += 1
print(divisor - 1)