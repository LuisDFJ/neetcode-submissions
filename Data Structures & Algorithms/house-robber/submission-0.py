class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        cache = {}
        def dfs( i : int ) -> int:
            if i in cache: return cache[i]
            money = 0
            for j in range(i+2,N):
                money = max(money,dfs(j))
            cache[i] = nums[i] + money
            return cache[i]

        m = 0
        for i in range(N):
            m = max(m,dfs(i))
        return m
        