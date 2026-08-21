class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        tab = [1,1]
        for i in range(1,n):
            tab[0], tab[1] = tab[1], tab[0] + tab[1]
        return tab[1]
        