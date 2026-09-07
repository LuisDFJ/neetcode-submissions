class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        return dfs(0,total//2,nums,{}) == total//2

def dfs(i:int,cap:int,nums:list[int],mem:dict) -> int:
    if i == len(nums): return 0
    if (i,cap) in mem: return mem[(i,cap)]
    res = dfs(i+1,cap,nums,mem)
    newCap = cap - nums[i]
    if newCap >= 0:
        p = nums[i] + dfs(i+1,newCap,nums,mem)
        res = max(res,p)
    mem[(i,cap)] = res
    return res
        