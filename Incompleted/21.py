def d(num):
    divisors = [i for i in range(1,num) if num % i == 0]
    if 10000 in divisors:
        return True
    else:
        return sum(divisors)

number = 1
total = 0
done = False

while not done:
    output = d(number)
    if output == True:
        done = True
    total += output
    number += 1
print(total)