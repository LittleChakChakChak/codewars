# 6kyu_kata
def to_camel_case(text):
    textFinal = ''
    for i in range(len(text)):
        if text[i-1] == '_' or text[i-1] == '-':
            textFinal += text[i].capitalize()
        elif text[i] != '_' and text[i] != '-':
            textFinal += text[i]
    return textFinal


print(to_camel_case("")) #"An empty string was provided but not returned")
print(to_camel_case("the_stealth_warrior")) # "to_camel_case('the_stealth_warrior') did not return correct value")
print(to_camel_case("The-Stealth-Warrior")) #"to_camel_case('The-Stealth-Warrior') did not return correct value")
print(to_camel_case("A-B-C")) # "to_camel_case('A-B-C') did not return correct value")