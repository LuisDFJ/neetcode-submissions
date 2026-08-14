

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        time = lambda k: sum([-(b//-k)for b in piles])
        left,right = 1,max(piles)
        res = right
        while left <= right:
            mid = (right+left)//2
            if time(mid) <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
        