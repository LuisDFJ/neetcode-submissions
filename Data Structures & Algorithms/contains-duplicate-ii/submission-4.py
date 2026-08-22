class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        L = 0
        s = set()
        for R in range(n):
            if R - L > k:
                s.remove(nums[L])
                L += 1
            if nums[R] in s: return True
            s.add(nums[R])

        return False
