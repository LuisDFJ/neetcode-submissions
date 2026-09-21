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
        def dfs(root:Optional[Node], key:int,val:int) -> Node:
            if not root:
                return Node(key,val)
            if key < root.key:
                root.left = dfs(root.left,key,val)
            elif key > root.key:
                root.right = dfs(root.right,key,val)
            else:
                root.val = val
            return root
        self.root = dfs(self.root,key,val)

    def get(self, key: int) -> int:
        def dfs(root:Optional[Node], key:int) -> int:
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
        def minNode(root:Node) -> Node:
            while root and root.left:
                root = root.left
            return root

        def dfs(root:Optional[Node], key:int) -> Optional[Node]:
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
                    successor = minNode(root.right)
                    root.key = successor.key
                    root.val = successor.val
                    root.right = dfs(root.right,successor.key)
            return root
        self.root = dfs(self.root,key)

    def getInorderKeys(self) -> List[int]:
        def dfs(root:Optional[Node],res:list):
            if not root: return
            dfs(root.left,res)
            res.append(root.key)
            dfs(root.right,res)
        res = []
        dfs(self.root,res)
        return res