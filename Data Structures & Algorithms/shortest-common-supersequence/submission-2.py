class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        a,b = str1, str2
        N,M = len(str1), len(str2)

        prev = [ a[i:] for i in range(N + 1) ]

        for j in range(M-1,-1,-1):
            curr = [ "" ] * N + [ b[j:] ]
            for i in range(N-1,-1,-1):
                if a[i] == b[j]:
                    curr[i] = a[i] + prev[i+1]
                else:
                    if len(curr[i+1]) < len(prev[i]):
                        curr[i] = a[i] + curr[i+1]
                    else:
                        curr[i] = b[j] + prev[i]
            prev = curr
        return prev[0]

