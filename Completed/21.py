def d(num):
    return sum([i for i in range(1,num) if num % i == 0])

a = 1
total = 0

while True:
    b = d(a)
    if a < 10000 or b < 10000:
        if d(b) == a and a != b:
            total += a
        a += 1
    else:
        break
    
print(total)