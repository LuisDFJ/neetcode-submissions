class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pool = set()
        for n in nums:
            if n in pool:
                return True
            pool.add(n)
        return False
