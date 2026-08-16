class Node:
    def __init__(self, key:int, val:int, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = Node(key,val)
            return
        def dfs(root: Node, key: int):
            nonlocal val
            if not root: return Node(key,val)
            if key < root.key:
                root.left = dfs(root.left,key)
            elif key > root.key:
                root.right = dfs(root.right,key)
            else:
                root.val = val
            return root
        dfs(self.root,key)

    def get(self, key: int) -> int:
        def dfs(root: Node, key: int) -> int:
            if not root: return -1
            if key < root.key:
                return dfs(root.left,key)
            elif key > root.key:
                return dfs(root.right,key)
            return root.val
        return dfs(self.root,key)

    def getMin(self) -> int:
        if not self.root: return -1
        node = self.root
        while node and node.left:
            node = node.left
        return node.val

    def getMax(self) -> int:
        if not self.root: return -1
        node = self.root
        while node and node.right:
            node = node.right
        return node.val

    def remove(self, key: int) -> None:
        def findMin(root: Node) -> Optional[Node]:
            node = root
            while node and node.left:
                node = node.left
            return node

        def dfs(root: Node, key: int) -> Optional[Node]:
            if not root: return None
            if key < root.key:
                root.left = dfs(root.left, key)
            elif key > root.key:
                root.right = dfs(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    successor = findMin(root.right)
                    # or findMax(root.left)
                    root.key = successor.key
                    root.val = successor.val
                    root.right = dfs(root.right, successor.key)
            return root
        self.root = dfs(self.root,key)

    def getInorderKeys(self) -> List[int]:
        res = []
        def dfs(root):
            nonlocal res
            if not root: return
            dfs(root.left)
            res.append(root.key)
            dfs(root.right)
        dfs(self.root)
        return res
