from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = set(nums)
        mcount = 0
        for n in nums:
            if n-1 not in snums:
                count = 1
                while n + count in snums:
                    count += 1
                if count > mcount:
                    mcount = count
        return mcount
