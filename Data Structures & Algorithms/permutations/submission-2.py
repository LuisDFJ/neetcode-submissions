class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            aux = []
            for perm in res:
                for j in range(len(perm)+1):
                    p = perm.copy()
                    p.insert(j,n)
                    aux.append(p)
            res = aux
        return res