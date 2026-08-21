class Solution:
    def rob(self, nums: List[int]) -> int:
        left,right = 0,0
        for n in nums:
            left,right = right, max(n+left,right)
        return right
        