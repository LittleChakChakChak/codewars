# 6kyu_kata
def find_uniq(arr):
    meeting = {}
    for i in arr:
        if meeting.get(i):
            items = meeting.get(i)
            meeting[i] = items+1
        else:
            meeting[i] = 1
    for key, value in meeting.items():
        if value == 1:
            return key

print(find_uniq([1, 1, 1, 2, 1, 1])) #2)
print(find_uniq([0, 0, 0.55, 0, 0])) #0.55)
print(find_uniq([0, 10, 3, 1, 0, 3])) #10)