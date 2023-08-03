# 7 kyu
def get_middle(s):
    if len(s) % 2 == 0:
        mid = int(len(s) / 2)
        chars = s[mid-1]+s[mid]
    else:
        chars = s[int(len(s)/2)]
    return chars


print(get_middle("test")) #"es")
print(get_middle("testing")) #"t")
print(get_middle("middle")) #"dd")
print(get_middle("A")) #"A")
print(get_middle("of")) #"of")