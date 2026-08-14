# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.dfs(pairs,0,len(pairs)-1)

    def dfs(self,arr: List[Pair], s: int, e: int) -> List[Pair]:
        if e-s > 0:
            left = s
            for i in range(s,e):
                if arr[i].key < arr[e].key:
                    arr[i],arr[left] = arr[left],arr[i]
                    left += 1
            arr[e],arr[left] = arr[left],arr[e]
            self.dfs(arr,s,left-1)
            self.dfs(arr,left+1,e)
        return arr