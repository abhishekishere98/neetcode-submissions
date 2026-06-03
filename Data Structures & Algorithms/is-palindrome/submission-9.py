class Solution:
    def isPalindrome(self, s: str) -> bool:
        revStr = ""
        for char in range (len(s)-1,-1,-1):
            if s[char].isalnum():
                revStr += s[char].lower()
            else:
                continue
        if revStr == revStr[::-1]:
            return True
        else:
            return False
        