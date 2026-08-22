class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        accum = 0
        threshold *= k
        res = 0
        for R in range(len(arr)):
            if R - L >= k:
                accum -= arr[L]
                L += 1
            accum += arr[R]
            if R - L == k - 1 and accum >= threshold: res += 1
        return res

