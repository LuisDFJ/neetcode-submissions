class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        stack = []
        def dfs( i : int, total : int ):
            if total == target:
                res.append(stack.copy())
                return
            if i == len(nums) or total > target:
                return

            stack.append(nums[i])
            dfs(i,total + nums[i])
            stack.pop()
            dfs(i + 1,total)
        
        dfs(0,0)
        return res
        