    
def word_count_engine(document):
    document = document.lower().split(' ')
    _dict = {}
    res = []
    # removing punctuations and other non-alphabetic characters
    charList = []
    for word in document:
        for ch in word:
            if (ch>='a' and ch<='z'):
                charList.append(ch)

        cleanWord = "".join(charList)
        charList = []

        if (len(cleanWord) < 1):
            continue

        if cleanWord in _dict:
            _dict[cleanWord] += 1
        else:
            _dict[cleanWord] = 1
    sortedWordList = sorted(_dict.items(), key=lambda x: x[1], reverse=True)

    for word, count in sortedWordList:
        res.append([word, str(count)])

    return res

# print (word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!"))

if __name__=="__main__":
    assert word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!")==[["practice", "3"], ["perfect", "2"], ["makes", "1"], ["youll", "1"], ["only", "1"],["get", "1"], ["by", "1"], ["just", "1"]], "Failled test 1"
    print("Passed all test cases!")

        