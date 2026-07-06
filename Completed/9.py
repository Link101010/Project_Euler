import math

for a in range(1000):
    for b in range(1000):
        if math.isqrt(a**2 + b**2) and a + b + math.sqrt(a**2 + b**2) == 1000:
            print(a * b * math.sqrt(a**2 + b**2))