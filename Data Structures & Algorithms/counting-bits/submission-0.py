class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            accum = 0
            while i > 0:
                accum += i & 1
                i = i >> 1
            res.append(accum)
        return res
        