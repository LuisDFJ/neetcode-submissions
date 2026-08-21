class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs( n:int, mem:dict ) -> int:
            if n in mem: return mem[n]
            if n <= 1: return 1
            mem[n] = dfs(n-1,mem) + dfs(n-2,mem)
            return mem[n]
        return dfs(n, {})
        