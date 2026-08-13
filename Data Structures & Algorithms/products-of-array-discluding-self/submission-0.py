from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1]
        prefix = [1]
        n = len(nums)
        for i in range(n):
            j = n - i - 1
            prefix.append( prefix[i] * nums[i] )
            suffix.append( suffix[i] * nums[j] )
        arr = []
        for i in range(n):
            j = n - i - 1
            arr.append( prefix[i] * suffix[j] )
        return arr
