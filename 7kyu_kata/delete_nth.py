# 6kyu_kata
def delete_nth(order,max_e):
    order.reverse()
    set_order = set(order)
    for i in set_order:
        if order.count(i) > max_e:
            e = order.count(i)
            e_del = e - max_e
            while e_del != 0:
                order.remove(i)
                e_del -= 1
    order.reverse()
    return order


# print(delete_nth([20,37,20,21], 1)) # [20,37,21])
# print(delete_nth([1,1,3,3,7,2,2,2,2], 3)) # [1, 1, 3, 3, 7, 2, 2, 2])

print(delete_nth([23, 9, 9, 39, 9, 9, 39, 23, 23, 5, 33, 23, 33, 9, 9, 23, 5, 9, 23, 9,
                  39, 23, 39, 23, 27, 39, 9, 23, 39, 33, 23], 1))

