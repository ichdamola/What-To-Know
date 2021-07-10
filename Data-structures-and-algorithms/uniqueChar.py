from collections import defaultdict

def uniqueChar(s):
    letter = defaultdict(int)
    for i in s:
        letter[i] += 1
    for i in range(len(s)):
        if letter[s[i]] < 2:
            return i
    return -1
