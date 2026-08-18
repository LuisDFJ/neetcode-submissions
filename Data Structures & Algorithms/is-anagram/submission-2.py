class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = {}
        for c in s:
            if c not in sCount:
                sCount[c] = 1
            else:
                sCount[c] += 1
        for c in t:
            if c not in sCount:
                return False
            else:
                sCount[c] -= 1
        for v in sCount.values():
            if v != 0: return False
        return True
        