# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge( s : int, m : int, e : int ):
            A = list(pairs[s:m+1])
            B = list(pairs[m+1:e+1])
            i = j = 0
            k = s
            while i < len(A) and j < len(B):
                if A[i].key <= B[j].key:
                    pairs[k] = A[i]
                    i += 1
                else:
                    pairs[k] = B[j]
                    j += 1
                k += 1
            while i < len(A):
                pairs[k] = A[i]
                i += 1
                k += 1
            while j < len(B):
                pairs[k] = B[j]
                j += 1
                k += 1

        def dfs(s : int, e : int):
            if e - s > 0:
                m = (s+e)//2
                dfs(s,m)
                dfs(m+1,e)
                merge(s,m,e)

        dfs(0,len(pairs)-1)
        return pairs

