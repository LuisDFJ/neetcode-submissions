class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        for i in range(n):
            accum = 0
            for j in range(i,i+n):
                accum += nums[j%n]
                res = max(res,accum)
        return res
        