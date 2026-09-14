class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = [c for c in s]
        t = []
        for i in range(len(s)):
            t = helper(i,i,s,t)
            t = helper(i,i+1,s,t)
        return "".join(t)



def helper(l:int,r:int,s:list[str],t:list[str]) -> list[str]:
    while l >= 0 and r < len(s) and s[r] == s[l]:
        length = r-l+1
        if len(t) <= length:
            t = s[l:r+1]
        l -= 1; r += 1
    return t