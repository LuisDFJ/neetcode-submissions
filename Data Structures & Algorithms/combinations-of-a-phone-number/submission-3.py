phone = {
    2 : "abc",
    3 : "def",
    4 : "ghi",
    5 : "jkl",
    6 : "mno",
    7 : "pqrs",
    8 : "tuv",
    9 : "wxyz",
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits: return res
        n = len(digits)
        def dfs(i:int,stack:List[str]):
            if len(stack) == n:
                res.append("".join(stack))
                return
            
            for c in phone[int(digits[i])]:
                stack.append(c)
                dfs(i+1,stack)
                stack.pop()
        dfs(0,[])
        return res
        