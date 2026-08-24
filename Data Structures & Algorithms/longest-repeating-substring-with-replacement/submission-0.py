from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        self.counter = defaultdict(int)
        L = 0
        length = 0

        for R in range(len(s)):
            self.counter[s[R]] += 1
            while (R-L+1) - self.maxCount() > k:
                self.counter[s[L]] -= 1
                L += 1
            length = max(length,R-L+1)
        return length

    # O(26) since key in [A,...,Z]
    def maxCount(self):
        m = 0
        for _, count in self.counter.items():
            m = max(m,count)
        return m
        
        