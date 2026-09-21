# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

def merge(l:int,r:int,pairs:List[Pair]):
    m = (l+r)//2
    A = pairs[l:m+1].copy()
    B = pairs[m+1:r+1].copy()
    i,j = 0,0
    k = l
    while i < len(A) and j < len(B):
        if A[i].key <= B[j].key:
            pairs[k] = A[i]
            i += 1
        else:
            pairs[k] =  B[j]
            j += 1
        k += 1
    while i < len(A):
        pairs[k] = A[i]
        k += 1; i += 1
    while j < len(B):
        pairs[k] = B[j]
        k += 1; j += 1

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def dfs(l:int,r:int):
            if l < r:
                m = (l+r)//2
                dfs(l,m)
                dfs(m+1,r)
                merge(l,r,pairs)
        dfs(0,len(pairs)-1)
        return pairs
