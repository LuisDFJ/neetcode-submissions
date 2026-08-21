class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        mem = {}
        def dfs( i : int ) -> int:
            if i in mem: return mem[i]
            if i >= N: return 0
            mem[i] = max( dfs(i+1), nums[i] + dfs(i+2) )
            return mem[i]
        return dfs(0)
        