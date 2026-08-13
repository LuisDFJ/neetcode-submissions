class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxAccum = 0
        accum = 0
        for n in nums:
            if n:
                accum += 1
            else:
                maxAccum = max(maxAccum,accum)
                accum = 0
        maxAccum = max(maxAccum,accum)
        return maxAccum
