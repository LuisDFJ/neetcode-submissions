class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        res = []
        for n,i in d.items():
            heapq.heappush(res,(i,n))
            if len(res) > k:
                heapq.heappop(res)
        return [ v for _,v in res  ]