class Node:
    def __init__(self,total:int,L:int,R:int):
        self.total = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

def build(nums:list[int],L:int,R:int) -> Node:
    if L == R: return Node(nums[L],L,R)
    root = Node(0,L,R)
    M = (L+R) // 2
    root.left = build(nums,L,M)
    root.right = build(nums,M+1,R)
    root.total = root.left.total + root.right.total
    return root
    
class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = build(nums,0,len(nums)-1)
    
    def update(self, index: int, val: int) -> None:
        def dfs(root, index, val):
            if root.L == root.R:
                root.total = val
                return
            M = (root.L+root.R)//2
            if index <= M:
                dfs( root.left, index, val )
            else:
                dfs( root.right, index, val )
            root.total = root.left.total + root.right.total
        dfs(self.root, index, val)
    
    def query(self, L: int, R: int) -> int:
        def dfs(root, L, R) -> int:
            if L == root.L and R == root.R:
                return root.total
            M = (root.L+root.R)//2
            if R <= M:
                return dfs(root.left,L,R)
            elif L > M:
                return dfs(root.right,L,R)
            else:
                return dfs(root.left,L,M) + dfs(root.right,M+1,R)
        return dfs(self.root,L,R)
                

