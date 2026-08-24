class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = L = 0
        length = len(nums) + 1
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                length = min(length,R-L+1)
                total -= nums[L]
                L += 1
        return 0 if length == len(nums)+1 else length
        

        