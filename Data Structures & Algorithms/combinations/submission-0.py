class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(i:int,stack:List[int]):
            if len(stack) == k:
                res.append(stack.copy())
                return
            if i > n:
                return
            stack.append(i)
            dfs(i+1,stack)
            stack.pop()
            dfs(i+1,stack)
        dfs(1,[])
        return res

        