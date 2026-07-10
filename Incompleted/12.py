def TriNum(num):
    return ((num)*(num + 1)) // 2

def NumOfDiv(num):
    return len([d for d in range(1, num + 1) if num % d == 0])

term = 1
while True:
    tnum = TriNum(term)
    if NumOfDiv(tnum) > 500:
        print(tnum)
        break
    else:
        term += 1