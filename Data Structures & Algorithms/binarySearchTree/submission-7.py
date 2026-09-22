class Node:
    def __init__(self,key:int, val:int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        def dfs(root:Optional[Node],key:int,val:int) -> Node:
            if not root: return Node(key,val)
            if key < root.key:
                root.left = dfs(root.left,key,val)
            elif key > root.key:
                root.right = dfs(root.right,key,val)
            else:
                root.val = val
            return root
        self.root = dfs(self.root,key,val)

    def get(self, key: int) -> int:
        def dfs(root:Optional[Node],key) -> int:
            if not root: return -1
            if key < root.key:
                return dfs(root.left,key)
            elif key > root.key:
                return dfs(root.right,key)
            else:
                return root.val
        return dfs(self.root,key)

    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        def findMin(curr:Node) -> Node:
            while curr and curr.left:
                curr = curr.left
            return curr
        def dfs(root:Node,key:int) -> Optional[Node]:
            if not root: return None
            if key < root.key:
                root.left = dfs(root.left,key)
            elif key > root.key:
                root.right = dfs(root.right,key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    succesor = findMin(root.right)
                    root.val = succesor.val
                    root.key = succesor.key
                    root.right = dfs(root.right,succesor.key)
            return root
        self.root = dfs(self.root,key)

    def getInorderKeys(self) -> List[int]:
        res = []
        def dfs(root:Optional[Node]):
            if not root: return
            dfs(root.left)
            res.append(root.key)
            dfs(root.right)
        dfs(self.root)
        return res

