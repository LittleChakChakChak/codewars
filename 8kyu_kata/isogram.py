# 7 kyu
def is_isogram(string):
    stringLower = string.lower()
    for char in stringLower:
        if stringLower.count(char) > 1:
            return False
    return True

print(is_isogram("Dermatoglyphics")) #True
print(is_isogram("isogram")) #True
print(is_isogram("aba")) #False
print(is_isogram("moOse")) #False
print(is_isogram("isIsogram")) #False
print(is_isogram("")) #True