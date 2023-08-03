# 5kyu_kata
def perimeter(n):
    fibonacci = 2
    a = 1
    b = 1
    i = 0
    while i < n-1:
        c = a + b
        b, a = a, c
        fibonacci += c
        i += 1
    return 4 * fibonacci

print(perimeter(5)) # , 80)
print(perimeter(7)) # , 216)
print(perimeter(20)) # , 114624)
print(perimeter(30)) # , 14098308)
print(perimeter(100)) # , 6002082144827584333104)
print(perimeter(500)) # , 236242502754228216753899909177020571216837162566
# 0854753765546783141099308400948230006358531927265833165504)