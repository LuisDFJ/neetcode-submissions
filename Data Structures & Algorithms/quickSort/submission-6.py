# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def dfs(left:int,right:int):
            if right > left:
                mid = left
                for i in range(left,right):
                    if pairs[i].key < pairs[right].key:
                        pairs[i],pairs[mid] = pairs[mid],pairs[i]
                        mid += 1
                pairs[right],pairs[mid] = pairs[mid],pairs[right]
                dfs(left,mid-1)
                dfs(mid+1,right)
        dfs(0,len(pairs)-1)
        return pairs
