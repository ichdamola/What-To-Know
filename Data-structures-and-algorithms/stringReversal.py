'''
# def string_reversal(str_):
#     if len(str_) == 0:
#         return ""

#     statement = str_.split(' ')
#     reversed_statement = statement[::-1]

#     return " ".join(reversed_statement)
'''

def string_reversal(str_):
    if len(str_) == 0:
        return ""
    
    str_without_spaces = []
    word = ""
    i = 0

    while i < len(str_):
        if (str_[i] >= "a" and str_[i] <='z') or (str_[i] >= 'A' and str_[i] <='Z'):
            word += str_[i]
        
        else:
            str_without_spaces.append(word)
            word = ""
        i += 1
    if word:
        str_without_spaces.append(word)  

    return " ".join(reversed(str_without_spaces))

if __name__ == "__main__":
    assert string_reversal("This is the best") == "best the is This", "Failed test case."