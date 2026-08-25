class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*(n+1)
        postfix = [1]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] * nums[i]
            postfix[n-1-i] = postfix[n-i] * nums[n-1-i]
        
        return [
            prefix[i] * postfix[i+1]
            for i in range(n)
        ]
        