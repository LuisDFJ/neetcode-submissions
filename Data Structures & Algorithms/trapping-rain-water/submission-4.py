class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left,right = 0,n-1
        lMax,rMax = height[left], height[right]

        res = 0
        while left < right:
            if height[left] < height[right]:
                left += 1
                lMax = max(lMax,height[left])
                res += lMax - height[left]
            else:
                right -= 1
                rMax = max(rMax,height[right])
                res += rMax - height[right]
        return res
        