class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums:List[int],stack:List[int]):
            if not nums:
                res.append(stack.copy())
                return
            
            for i,n in enumerate(nums):
                stack.append(n)
                nCopy = nums.copy()
                nCopy.pop(i)
                dfs(nCopy,stack)
                stack.pop()
        dfs(nums,[])
        return res

        