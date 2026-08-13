from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [ [] for _ in range(len(nums) + 1) ]
        for key,freq in count.items():
            bucket[freq].append(key)
        res = []
        c = 0
        while bucket and c < k:
            if bucket[-1]:
                v = bucket[-1].pop()
                res.append(v)
                c += 1
            else:
                bucket.pop()
        return res

