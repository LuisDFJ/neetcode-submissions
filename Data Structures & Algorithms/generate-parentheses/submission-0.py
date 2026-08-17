class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def dfs(openN : int, closeN : int):
            if not openN and not closeN:
                res.append("".join(stack))
                return
            
            if openN > 0:
                stack.append("(")
                dfs(openN-1,closeN)
                stack.pop()
            if openN < closeN:
                stack.append(")")
                dfs(openN,closeN-1)
                stack.pop()
        
        dfs(n,n)
        return res

        