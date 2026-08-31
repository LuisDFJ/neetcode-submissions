class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i:int,total:int,stack:List[int]):
            if total == target:
                res.append(stack.copy())
                return
            if i == len(nums) or total > target:
                return
            
            for j in range(i,len(nums)):
                stack.append(nums[j])
                dfs(j,total+nums[j],stack)
                stack.pop()
        dfs(0,0,[])
        return res
        