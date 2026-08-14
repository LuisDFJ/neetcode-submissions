class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3
        for n in nums:
            buckets[n] += 1
        i = 0
        for n,bucket in enumerate(buckets):
            for _ in range(bucket):
                nums[i] = n
                i += 1
        