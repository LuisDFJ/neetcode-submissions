from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapify(heap)
        while len(heap) > 1:
            s1 = heappop(heap)
            s2 = heappop(heap)
            s3 = abs(s1-s2)
            if s3 > 0:
                heappush(heap,-s3)
        if len(heap) == 0:
            return 0
        return -heappop(heap)

        