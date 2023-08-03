# 4 kyu
def solution(string,markers):
    string_list = string.split("\n")
    finaly_list = []

    for item in string_list:
        word = ""
        for char in item:
            if char in markers:
                break
            else:
                word = word + char
        finaly_list.append(word.rstrip())
    return "\n".join(finaly_list)



print(solution('\tapples, pears # and bananas \ngrapes\nbananas !apples', ['#', '!'])) # 'apples, pears\ngrapes\nbananas')
print(solution('a #b\nc\nd $e f g', ['#', '$'])) # 'a\nc\nd')
print(solution(' a #b\nc\nd $e f g', ['#', '$'])) # ' a\nc\nd')