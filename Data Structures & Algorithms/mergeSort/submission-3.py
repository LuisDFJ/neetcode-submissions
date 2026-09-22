# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def dfs(left:int,right:int):
            if right > left:
                mid = (right+left)//2
                dfs(left,mid)
                dfs(mid+1,right)
                merge(left,mid,right,pairs)
        dfs(0,len(pairs)-1)
        return pairs

def merge(left:int,mid:int,right:int,pairs:list[Pair]):
    a = pairs[left:mid+1].copy()
    b = pairs[mid+1:right+1].copy()
    i = j = 0
    k = left
    while i < len(a) and j < len(b):
        if a[i].key <= b[j].key:
            pairs[k] = a[i]
            i += 1
        else:
            pairs[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        pairs[k] = a[i]
        i += 1; k += 1
    while j < len(b):
        pairs[k] = b[j]
        j += 1; k += 1
