class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0]*n
        rightMax = [0]*n
        leftMax[0] = height[0]
        rightMax[n-1] = height[n-1]
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i])
            rightMax[n-1-i] = max(rightMax[n-i],height[n-1-i])
        water = 0
        for i in range(1,len(height)-1):
            water += max(0,min(leftMax[i-1],rightMax[i+1])-height[i])
        return water

    #def trap(self, height: List[int]) -> int:
        #water = 0
        #for i in range(1,len(height)-1):
            #leftMax = max(height[:i])
            #rightMax = max(height[i+1:])
            #water += max(0,min(leftMax,rightMax)-height[i])
        #return water

        