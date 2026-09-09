class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        cache = {}
        def dfs(i:int) -> int:
            if i == n: return 0
            if i in cache: return cache[i]

            res = costs[0] + dfs(i+1)
            
            j = i
            while j < n and days[i] + 7 > days[j]:
                j += 1
            res = min(res, costs[1] + dfs(j))

            j = i
            while j < n and days[i] + 30 > days[j]:
                j += 1
            res = min(res, costs[2] + dfs(j))
            cache[i] = res
            return res
        return dfs(0)
        