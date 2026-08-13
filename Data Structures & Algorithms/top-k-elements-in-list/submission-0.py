import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        pq = []
        for key,freq in count.items():
            heapq.heappush(pq,(-freq,key))
        res = []
        for _ in range(k):
            _,k = heapq.heappop(pq)
            res.append(k)
        return res
