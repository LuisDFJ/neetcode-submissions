class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i:int) -> List[List[int]]:
            if i == len(nums):
                return [[]]
            
            res = []
            for perm in dfs(i+1):
                for j in range(len(perm)+1):
                    p = perm.copy()
                    p.insert(j,nums[i])
                    res.append(p)
            return res
        return dfs(0)

        