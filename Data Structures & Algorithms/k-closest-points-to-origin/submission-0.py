from heapq import heappush, heappop

def distance(a : List[int]) -> float:
    return a[0]** 2 + a[1]** 2 # Square Root is not necessary
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        for p in points:
            heappush(queue, (distance(p),p))
        return [ heappop(queue)[1] for _ in range(k)]