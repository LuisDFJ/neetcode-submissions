class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        l = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j,k = i+1,n-1
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                if res == 0:
                    l.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif res < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        return l
                    
        