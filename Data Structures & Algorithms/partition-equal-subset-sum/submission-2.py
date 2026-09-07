class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        cache = {}
        def dfs(i:int,t:int):
            if t == target: return True
            if i == len(nums): return False
            if (i,t) in cache: return cache[(i,t)]
            res = dfs(i+1,t+nums[i]) or dfs(i+1,t)
            cache[(i,t)] = res
            return res
        return dfs(0,0)