    
def word_count_engine(document):
    wordCountPair = {}

    # Tokenizing the words
    document = document.lower().split(' ')

    # removing non-alphabetic characters
    for word in document:
        charList = []
        for ch in word:
            if (ch>='a' and ch<='z'):
                charList.append(ch)

        # convert charList to word
        cleanWord = "".join(charList)
        charList = []

        if len(cleanWord) < 1:
            continue

        # creating the wordCountPair
        if cleanWord in wordCountPair:
            wordCountPair[cleanWord] += 1
        else:
            wordCountPair[cleanWord] = 1
    
    # sorting the words based on their number of occurences in desending order
    sortedWordCountPair = sorted(wordCountPair.items(), key=lambda x:x[1], reverse=True)

    res = []

    for word,count in sortedWordCountPair:
        res.append([word, str(count)])
    
    return res

# print(word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!"))

# TC: O(n^2lgn) | SC: O(n^2)
if __name__=="__main__":
    assert word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!")==[["practice", "3"], ["perfect", "2"], ["makes", "1"], ["youll", "1"], ["only", "1"],["get", "1"], ["by", "1"], ["just", "1"]], "Failled test 1"
    print("Passed all test cases!")

        