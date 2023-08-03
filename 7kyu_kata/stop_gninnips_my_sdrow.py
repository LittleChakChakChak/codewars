# 6kyu_kata
def spin_words(sentence):
    words = sentence.split(' ')
    final_words = ''
    for char in words:
        if len(char) >= 5:
            char = ''.join(reversed(char))
        final_words = final_words + ' ' + char
    return final_words.rstrip().lstrip()


print(spin_words("Welcome")) # "emocleW")
print(spin_words("to")) # "to")
print(spin_words("CodeWars")) # "sraWedoC")
print(spin_words("Hey fellow warriors")) # "Hey wollef sroirraw")
print(spin_words("This sentence is a sentence")) # "This ecnetnes is a ecnetnes")

