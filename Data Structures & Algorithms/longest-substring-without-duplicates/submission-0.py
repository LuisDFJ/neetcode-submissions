class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        chars = set()
        length = 0
        for R in range(len(s)):
            while s[R] in chars:
                chars.remove(s[L])
                L += 1
            chars.add(s[R])
            length = max(length,R-L+1)
        return length
        