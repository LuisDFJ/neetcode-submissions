class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        resMax = nums[0]
        accMax = 0

        resMin = nums[0]
        accMin = 0

        total = 0

        for n in nums:
            total += n
            accMax = max(accMax,0) + n
            resMax = max(resMax,accMax)
            accMin = min(accMin,0) + n
            resMin = min(resMin,accMin)
        
        if resMax > 0:
            return max( resMax, total - resMin )
        return resMax

