class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mSum = nums[0]
        accum = 0
        for n in nums:
            accum = max(accum,0) + n
            mSum = max(mSum,accum)
        return mSum
            
        