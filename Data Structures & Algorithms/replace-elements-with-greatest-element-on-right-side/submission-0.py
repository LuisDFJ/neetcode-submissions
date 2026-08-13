class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for n in range(len(arr)-1):
            res.append( max(arr[n+1:]) )
        res.append(-1)
        return res
