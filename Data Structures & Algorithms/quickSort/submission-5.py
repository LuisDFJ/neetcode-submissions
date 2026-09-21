# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
def dfs(pairs: List[Pair], l:int, r :int):
    if r > l:
        m = l
        for i in range(l,r):
            if pairs[i].key < pairs[r].key:
                pairs[i],pairs[m] = pairs[m],pairs[i]
                m += 1
        pairs[r],pairs[m] = pairs[m],pairs[r]
        dfs(pairs,l,m-1)
        dfs(pairs,m+1,r)
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        dfs(pairs,0,len(pairs)-1)
        return pairs
        