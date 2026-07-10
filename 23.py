import math, random

data = [i for i in range(10)]
abs_position = 1000000
starting_number = 0
count = 0
while True:
    if math.factorial(len(data) - 1) * count < 1000000:
        count += 1
    else:
        break
count -= 1
rel_position = abs_position - math.factorial(len(data) - 1) * count
small_data = [x for x in data].remove(data[count - 1])

small_data_perms = []
amount = math.factorial(len(small_data))
perm_count = 0
while perm_count < amount:
    choose = [str(x) for x in small_data]
    for i in range(len(small_data)):
        perm = ''
        num = random.choice(choose)
        perm += num
        choose.remove(num)
    if perm not in small_data_perms:
        small_data_perms.append(int(num))
        perm_count += 1

ordered_small_data_perms = small_data_perms.sort()
print(int(f'{data[count - 1]}{ordered_small_data_perms[rel_position]}'))