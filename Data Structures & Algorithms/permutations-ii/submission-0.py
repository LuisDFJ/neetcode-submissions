class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        res = []
        def dfs(i:int, stack:List[int]):
            if i == len(nums):
                res.append(stack.copy())
                return
            for n in counter:
                if counter[n] > 0:
                    counter[n] -= 1
                    stack.append(n)
                    dfs(i+1,stack)
                    stack.pop()
                    counter[n] += 1
        dfs(0,[])
        return res




        