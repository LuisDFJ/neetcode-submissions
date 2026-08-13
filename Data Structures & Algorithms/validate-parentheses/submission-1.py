def isMatch(a : str, b : str) -> bool:
    return (
        ( a == "(" and b == ")" ) or
        ( a == "{" and b == "}" ) or
        ( a == "[" and b == "]" ) 
    )


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif len(stack) and isMatch( stack.pop(), c ):
                continue
            else:
                return False
        return not stack