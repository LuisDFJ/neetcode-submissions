class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def sign(i: int) -> tuple[bool,bool]:
            r = arr[i] - arr[i-1]
            if r == 0: return True,False
            else: return False, True if r > 0 else False
        
        L = 0
        prev = None
        length = 1
        for R in range(1,len(arr)):
            isZero, s = sign(R)
            if isZero:
                L = R
            elif prev is not None and not prev ^ s:
                L = R - 1
            prev = s

            length = max(length,R-L+1)
        return length
