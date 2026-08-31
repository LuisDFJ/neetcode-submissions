class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i:int,stack:List[int]):
            if len(stack) == k:
                res.append(stack.copy())
                return
            if i > n:
                return
            
            for j in range(i,n+1):
                stack.append(j)
                dfs(j+1,stack)
                stack.pop()
        dfs(1,[])
        return res
        