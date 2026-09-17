class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            complement = target - n
            if complement in d:
                return [d[complement],i]
            d[n] = i
        return []