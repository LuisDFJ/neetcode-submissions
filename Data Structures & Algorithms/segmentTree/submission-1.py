class Node:
    def __init__(self,total,L,R) -> None:
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    def update(self,index:int,val:int) -> None:
        if self.L == self.R:
            self.sum = val
            return
        M = (self.L+self.R) // 2
        if index <=  M:
            self.left.update(index,val)
        else:
            self.right.update(index,val)
        self.sum = self.left.sum + self.right.sum
    
    def query(self,L:int,R:int) -> int:
        if L == self.L and R == self.R: return self.sum
        M = (self.L+self.R)  // 2
        if L > M:
            return self.right.query(L,R)
        elif R <= M:
            return self.left.query(L,R)
        else:
            return self.left.query(L,M) + self.right.query(M+1,R)

def build(nums:List[int], L:int,R:int) -> Node:
    if L == R: return Node(nums[L],L,R)
    M = (L+R)//2
    root = Node(0,L,R)
    root.left = build(nums,L,M)
    root.right = build(nums,M+1,R)
    root.sum = root.left.sum + root.right.sum
    return root

class SegmentTree:
    def __init__(self, nums: List[int]):
        self.root = build(nums,0,len(nums)-1)
    
    def update(self, index: int, val: int) -> None:
        self.root.update(index,val)
    
    def query(self, L: int, R: int) -> int:
        return self.root.query(L,R)