# 6kyu_kata
def tower_builder(n_floors):
    max_n = n_floors
    building = []
    n = 1
    while n_floors:
        building.append((' '* int(max_n-n/2)) + ('*'*n) + (' '* int(max_n-n/2)))
        n_floors -= 1
        n += 2
    return building

print(tower_builder(1)) # ['*', ])
print(tower_builder(2)) # [' * ', '***'])
print(tower_builder(3)) # ['  *  ', ' *** ', '*****'])