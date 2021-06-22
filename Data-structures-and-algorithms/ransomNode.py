from collections import defaultdict

class Solution(object):
    def canSpell(self, magazine, note):
        letter = defaultdict(int)
        for c in magazine:
            letter[c] += 1
        for c in note:
            if letter[c] <= 0:
                return False
            letter[c] -= 1
        return True

print(Solution().canSpell(['a', 'b', 'c', 'd', 'e', 'f'], 'bed'))
#True

print(Solution().canSpell(['a', 'b', 'c', 'e', 'd', 'f'], 'cat'))
#False