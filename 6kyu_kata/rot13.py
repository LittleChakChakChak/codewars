# 5kyu_kata
def rot13(message):
    new_message = ''
    code_rot13 = {'a': 'n', 'n': 'a', 'b': 'o', 'o': 'b', 'c': 'p', 'p': 'c', 'd': 'q', 'q': 'd', 'e': 'r',
                  'r': 'e', 'f': 's', 's': 'f', 'g': 't', 't': 'g', 'h': 'u', 'u': 'h', 'i': 'v', 'v': 'i',
                  'j': 'w', 'w': 'j', 'k': 'x', 'x': 'k', 'l': 'y', 'y': 'l', 'm': 'z', 'z': 'm',
                  # -------------
                  'A': 'N', 'N': 'A', 'B': 'O', 'O': 'B', 'C': 'P', 'P': 'C', 'D': 'Q', 'Q': 'D', 'E': 'R',
                  'R': 'E', 'F': 'S', 'S': 'F', 'G': 'T', 'T': 'G', 'H': 'U', 'U': 'H', 'I': 'V', 'V': 'I',
                  'J': 'W', 'W': 'J', 'K': 'X', 'X': 'K', 'L': 'Y', 'Y': 'L', 'M': 'Z', 'Z': 'M'
                  }
    for char in message:
        if code_rot13.get(char):
            new_message += code_rot13.get(char)
        else:
            new_message += char
    return new_message

print(rot13("EBG13 rknzcyr.")) #, "ROT13 example.")
print(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,"
            "\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.")) #"Ubj pna lbh gryy na rkgebireg sebz na
# \nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
print(rot13("123")) #, "123")
print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"))#
                   # "This is actually the first kata I ever made. Thanks for finishing it! :)")
print(rot13("@[`{")) # "@[`{")