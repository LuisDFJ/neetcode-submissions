class Solution:
    def hammingWeight(self, n: int) -> int:
        accum = 0
        while n > 0:
            accum += n & 1
            n = n >> 1
        return accum
        