class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        N = len(nums)
        m = nums[0]
        for i in range(N):
            accum = 0
            for j in range(i,i + N):
                accum += nums[j%N]
                m = max(m,accum)
        return m


        