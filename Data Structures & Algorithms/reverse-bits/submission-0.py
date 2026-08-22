class Solution:
    def reverseBits(self, n: int) -> int:
        accum = 0
        for i in range(31,-1,-1):
            accum |= (n & 1) << i
            n = n >> 1
        return accum
