# 6kyu_kata
def is_pangram(s):
    return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())

print(is_pangram("The quick, brown fox jumps over the lazy dog!")) #True)
print(is_pangram("1bcdefghijklmnopqrstuvwxyz")) #False)
print(is_pangram("This isn't a pangram!")) #False)