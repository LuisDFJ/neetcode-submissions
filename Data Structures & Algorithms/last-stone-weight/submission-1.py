from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapify(heap)
        while len(heap) > 1:
            s1 = heappop(heap)
            s2 = heappop(heap)
            if s2 > s1:
                heappush(heap,s1 - s2)
        if len(heap) == 0:
            return 0
        return -heappop(heap)

        