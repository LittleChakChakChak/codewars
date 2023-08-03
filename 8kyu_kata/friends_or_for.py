# 7 kyu
def friend(x):
    myFriends = []
    for i in x:
        if len(i) == 4:
            myFriends.append(i)
    return myFriends


print(friend(["Ryan", "Kieran", "Mark",])) #["Ryan", "Mark"]
print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"])) #["Ryan"]
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"])) #["Jimm", "Cari", "aret"]