class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(i:int,nums:List[int],stack:List[int]):
            if i == len(nums):
                res.append(stack.copy())
                return
            stack.append(nums[i])
            dfs(i+1,nums,stack)
            stack.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1,nums,stack)
        
        dfs(0,sorted(nums),[])
        return res
        