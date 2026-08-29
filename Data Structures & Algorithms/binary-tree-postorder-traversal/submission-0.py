# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        stack = [root]
        visit = [False]
        res = []
        while stack:
            node,flag = stack.pop(),visit.pop()
            if flag:
                res.append(node.val)
            else:
                stack.append(node)
                visit.append(True)
                if node.right:
                    stack.append(node.right)
                    visit.append(False)
                if node.left:
                    stack.append(node.left)
                    visit.append(False)
        return res


        