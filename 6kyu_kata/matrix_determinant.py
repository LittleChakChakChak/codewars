# 4 kyu
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    # a * det(a_minor) - b * det(b_minor) + c * det(c_minor)
    result = 0
    for index, value in enumerate(matrix[0]):
        result += ((-1) ** index) * value * determinant(minor(matrix, 0, index))
    return result


def minor(mtx, y, x):
    result = []
    x_row = []
    for index_i, item_i in enumerate(mtx):
        if index_i != y:
            for index_j, item_j in enumerate(item_i):
                if index_j != x:
                    x_row.append(item_j)
            result.append(x_row)
            x_row = []
    return result

m1 = [[4, 6], [3,8]]
m5 = [[2,4,2],[3,1,1],[1,2,0]]
print(determinant([[5]])) # 5, "Determinant of a 1 x 1 matrix yields the value of the one element")\
print(determinant(m1)) # 14, "Should return 4*8 - 3*6, i.e. 14")\
print(determinant([[2,4,2],[3,1,1],[1,2,0]])) # 10, "Should return the determinant of [[2,4,2],[3,1,1],[1,2,0]], i.e. 10")
print('happy end')