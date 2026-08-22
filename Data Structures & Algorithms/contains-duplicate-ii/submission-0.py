class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k = k + 1
        n = len(nums)
        for L in range(n):
            for R in range(L+1,min(n,L+k)):
                if nums[L] == nums[R]: return True
        return False
        