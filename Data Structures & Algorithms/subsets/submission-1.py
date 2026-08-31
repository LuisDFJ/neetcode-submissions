class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i:int,nums:List[int],stack:List[int]):
            if i == len(nums):
                res.append(stack.copy())
                return
            stack.append(nums[i])
            dfs(i+1,nums,stack)
            stack.pop()
            dfs(i+1,nums,stack)
        

        dfs(0,nums,[])
        return res
        