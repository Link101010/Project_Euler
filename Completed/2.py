a = 1
b = 2
nums = []
while a <= 4000000:
    nums.append(a) if a % 2 == 0 else 0
    b, a = a + b, b
print(sum(nums))