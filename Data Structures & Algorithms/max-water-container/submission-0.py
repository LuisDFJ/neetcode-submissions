class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = lambda L,R: (R-L) * min(heights[R],heights[L])

        L,R = 0,len(heights)-1
        maxA = 0
        while L < R:
            A = area(L,R)
            maxA = max(maxA,A)
            if heights[L] < heights[R]: L += 1
            else: R -= 1
        return maxA

        