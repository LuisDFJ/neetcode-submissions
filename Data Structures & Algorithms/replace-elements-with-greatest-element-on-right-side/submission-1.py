class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0 for _ in range(n)]
        mnum = -1
        for n in range(n-1,-1,-1):
            res[n] = mnum
            if arr[n] > mnum:
                mnum = arr[n]
        return res
