class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n+1)
        postfix = [0] * (n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            postfix[n-1-i] = postfix[n-i] + nums[n-1-i]
        
        for i in range(n):
            if prefix[i+1] == postfix[i]:
                return i
        return -1

        