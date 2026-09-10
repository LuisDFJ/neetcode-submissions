class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)
        prev = [0] * (M+1)

        for i in range(N):
            curr = [0] * (M+1)
            for j in range(M):
                if text1[i] == text2[j]:
                    curr[j+1] = 1 + prev[j]
                else:
                    curr[j+1] = max(prev[j+1],curr[j])
            prev = curr
        return prev[-1]