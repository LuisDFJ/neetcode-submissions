class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counter = defaultdict(int)

        def maxCounter() -> int:
            m = 0
            for _,v in counter.items():
                m = max(m,v)
            return m
        
        l = 0
        length = 0
        for r in range(len(s)):
            counter[s[r]] += 1
            while (r-l+1) - maxCounter() > k:
                counter[s[l]] -= 1
                l += 1
            length = max(length,r-l+1)
        return length
            
        