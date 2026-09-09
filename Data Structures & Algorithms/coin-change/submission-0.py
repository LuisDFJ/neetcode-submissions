class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dfs(amount:int) -> int:
            if amount == 0:
                return 0
            if amount in cache: return cache[amount]
            
            res = 1e9
            for coin in coins:
                newAmount = amount - coin
                if newAmount >= 0:
                    res = min(res,1+dfs(newAmount))
            cache[amount] = res
            return res
        
        res = dfs(amount)
        return -1 if res >= 1e9 else res