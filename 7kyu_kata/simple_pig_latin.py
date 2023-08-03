# 6kyu_kata
def pig_it(text):
    words = text.split(' ')
    final_words = ''
    for char in words:
        if char != '!' and char != '?':
            char_list = list(char)
            char_list.append(char_list[0])
            char_list.remove(char_list[0])
            final_char = ''
            for i in char_list:
                final_char = final_char + i
            final_char = final_char + 'ay'
            final_words = final_words + final_char + ' '
        else:
            final_words = final_words + char
    return final_words.rstrip()



#print(pig_it('Pig latin is cool')) #'igPay atinlay siay oolcay')
print(pig_it('O tempora o mores !')) #'Oay emporatay oay oresmay !'')