class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        subStr = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in subStr:
                subStr.remove(s[l])
                l += 1
            subStr.add(s[r])
            result = max(result, (r-l)+1)
        
        return result
