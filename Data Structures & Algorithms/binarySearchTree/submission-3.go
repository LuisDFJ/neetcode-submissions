type Node struct {
    Key int
    Val int
    Left *Node
    Right *Node
}

func NewNode(key,val int) *Node {
    return &Node{Key:key,Val:val,Left:nil,Right:nil}
}

type TreeMap struct {
    Root *Node
}

func NewTreeMap() *TreeMap {
    return &TreeMap{Root:nil}
}

func (tm *TreeMap) Insert(key, val int) {
    var dfs func(*Node) *Node
    dfs = func(root *Node) *Node {
        if root == nil { return NewNode(key,val) }
        if key < root.Key {
            root.Left = dfs(root.Left)
        } else if key > root.Key {
            root.Right = dfs(root.Right)
        } else {
            root.Val = val
        }
        return root
    }
    tm.Root = dfs(tm.Root)
}

func (tm *TreeMap) Get(key int) int {
    var dfs func(*Node) int
    dfs = func(root *Node) int {
        if root == nil { return -1 }
        if key <  root.Key {
            return dfs(root.Left)
        } else if key > root.Key {
            return dfs(root.Right)
        } else {
            return root.Val
        }
    }
    return dfs(tm.Root)
}

func (tm *TreeMap) GetMin() int {
    if tm.Root == nil { return -1 }
    node := tm.Root
    for node != nil && node.Left != nil {
        node = node.Left
    }
    return node.Val
}

func (tm *TreeMap) GetMax() int {
    if tm.Root == nil { return -1 }
    node := tm.Root
    for node != nil && node.Right != nil {
        node = node.Right
    }
    return node.Val
}

func (tm *TreeMap) Remove(key int) {
    findMin := func(root *Node) *Node {
        node := root
        for node != nil && node.Left != nil {
            node = node.Left
        }
        return node
    }

    var dfs func(*Node, int) *Node
    dfs = func(root *Node, key int) *Node {
        if root == nil { return nil }
        if key < root.Key {
            root.Left =  dfs(root.Left,key)
        } else if key > root.Key {
            root.Right =  dfs(root.Right,key)
        } else {
            if root.Left == nil {
                return root.Right
            } else if root.Right == nil {
                return root.Left
            } else {
                successor := findMin(root.Right)
                root.Key = successor.Key
                root.Val = successor.Val
                root.Right = dfs(root.Right, successor.Key)
            }
        }
        return root
    }
    tm.Root = dfs(tm.Root,key)
}

func (tm *TreeMap) GetInorderKeys() []int {
    res := []int{}
    var dfs func(*Node)
    dfs = func(root *Node) {
        if root == nil { return }
        dfs(root.Left)
        res = append(res,root.Key)
        dfs(root.Right)
    }
    dfs(tm.Root)
    return res
}
