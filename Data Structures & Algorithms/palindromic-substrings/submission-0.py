class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += helper(i,i,s)
            res += helper(i,i+1,s)
        return res

def helper(l:int,r:int,s:str) -> int:
    res = 0
    while l >= 0 and r < len(s) and s[l] == s[r]:
        res += 1; l -= 1; r += 1
    return res