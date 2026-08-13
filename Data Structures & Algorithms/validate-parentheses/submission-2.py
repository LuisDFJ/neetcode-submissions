
hash_map = {
    "(" : ")",
    "[" : "]",
    "{" : "}",
}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in hash_map:
                stack.append(c)
            elif len(stack) and hash_map[stack.pop()] == c:
                continue
            else:
                return False
        return not stack