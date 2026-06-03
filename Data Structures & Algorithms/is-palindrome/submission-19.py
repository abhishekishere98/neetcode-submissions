class Solution:
    def isalphanum(self, c):
        return (
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9')
        )
    def isPalindrome(self, s: str) -> bool:
        # revStr = ""
        # for char in range (len(s)-1,-1,-1):
        #     if s[char].isalnum():
        #         revStr += s[char].lower()
        #     else:
        #         continue
        # if revStr == revStr[::-1]:
        #     return True
        # else:
        #     return False
        l,r = 0, len(s)-1

        while l<r :
            while l<r and not self.isalphanum(s[l]):
                l += 1
            while l<r and not self.isalphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        