i = 1
sum = 0
while i < 641000:
    sum += i**2 if i % 2 != 0 else 0
    i += 1
print(sum)