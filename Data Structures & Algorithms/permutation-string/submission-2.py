class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        counterS1 = defaultdict(int)
        for s in s1:
            counterS1[s] += 1

        counterS2 = defaultdict(int)
        for i in range(len(s1)):
            counterS2[s2[i]] += 1
        
        def compare() ->  bool:
            for c,v in counterS1.items():
                if counterS2[c] != v:
                    return False
            return True

        if compare(): return True
        for r in range(len(s1),len(s2)):
            counterS2[s2[r]] += 1
            counterS2[s2[r-len(s1)]] -= 1
            if compare(): return True
        return False

        