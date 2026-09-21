# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
def dfs(left:int,right:int,pairs:List[Pair]):
    if right > left:
        m = left
        for i in range(left,right):
            if pairs[i].key < pairs[right].key:
                pairs[i],pairs[m] = pairs[m],pairs[i]
                m += 1
        pairs[right],pairs[m] = pairs[m],pairs[right]
        dfs(left,m-1,pairs)
        dfs(m+1,right,pairs)

class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        dfs(0,len(pairs)-1,pairs)
        return pairs
        