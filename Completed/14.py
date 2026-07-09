def Collatz(n, count):
    if n == 1:
        return count
    elif n % 2 == 0:
        return Collatz(n // 2, count + 1)
    else:
        return Collatz(3 * n + 1, count + 1)

num, max_chain_len = 0, 0

for i in range(1,1000000):
    temp_chain_len = Collatz(i, 1)
    if temp_chain_len > max_chain_len:
        num, max_chain_len = i, temp_chain_len

print(num)
