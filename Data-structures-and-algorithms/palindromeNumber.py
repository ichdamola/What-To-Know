def isPalindrome(self, x: int) -> bool:
        return list(str(x))[::-1] == list(str(x))