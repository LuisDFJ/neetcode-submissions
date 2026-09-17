class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n+1)
        postfix = [1] * (n+1)
        for i in range(n):
            prefix[i+1] = nums[i] * prefix[i]
        for i in range(n-1,-1,-1):
            postfix[i] = nums[i] * postfix[i+1]
        
        return [
            prefix[i] * postfix[i+1]
            for i in range(n)
        ]