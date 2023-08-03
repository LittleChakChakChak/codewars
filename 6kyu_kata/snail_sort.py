# 4kyu
def snail(snail_map):
    results = []
    while len(snail_map) > 0:
        # направление вправо
        results += snail_map[0]
        del snail_map[0]

        if len(snail_map) > 0:
            # направление вниз
            for i in snail_map:
                results += [i[-1]]
                del i[-1]

            # направление влево
            if snail_map[-1]:
                results += snail_map[-1][::-1]
                del snail_map[-1]

            # направление вверх
            for i in reversed(snail_map):
                results += [i[0]]
                del i[0]

    return results



array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
print(snail(array))# expected)

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
expected = [1,2,3,4,5,6,7,8,9]
print(snail(array))# expected)