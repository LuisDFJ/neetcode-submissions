class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = lambda left,right : min(heights[left],heights[right]) * (right - left)
        left, right = 0,len(heights)-1
        m = 0
        while left < right:
            a = area(left,right)
            m = max(m,a)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return m
        