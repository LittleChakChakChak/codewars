# 6kyu_kata
def dig_pow(n, p):
    integers = list(str(n))
    sum = 0
    for i in integers:
        sum = sum + int(i) ** p
        p += 1
    if sum % n == 0:
        return int(sum / n)
    else:
        return -1

print(dig_pow(89, 1)) # 1)
print(dig_pow(92, 1)) # -1)
print(dig_pow(46288, 3)) # 51)
print(dig_pow(41, 5)) # 25)
print(dig_pow(114, 3)) # 9)
print(dig_pow(8, 3)) # 64)