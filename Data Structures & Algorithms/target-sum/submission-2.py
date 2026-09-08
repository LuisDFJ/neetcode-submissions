class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i:int,total:int,mem:dict) -> int:
            if i == len(nums):
                return 1 if total == target else 0
            if (i,total) in mem: return mem[(i,total)]
            res = 0
            for v in [nums[i],-nums[i]]:
                res += dfs(i+1,total+v,mem)
            mem[(i,total)] = res
            return res
        return dfs(0,0,{})
