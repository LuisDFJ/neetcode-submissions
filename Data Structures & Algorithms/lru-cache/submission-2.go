type Node struct {
    key, val int
    next, prev *Node
}

func NewNode(key,val int) *Node {
    return &Node{key:key,val:val,next:nil,prev:nil}
}

type LRUCache struct {
    cache map[int]*Node
    head, tail *Node
    capacity int
}

func Constructor(capacity int) LRUCache {
    res := LRUCache {
        cache: map[int]*Node {},
        head: NewNode(0,0),
        tail: NewNode(0,0),
        capacity: capacity,
    }
    res.head.next = res.tail
    res.tail.prev = res.head
    return res
}

func (this *LRUCache) remove(node *Node) {
    next,prev := node.next, node.prev
    next.prev, prev.next = prev, next
}

func (this *LRUCache) insert(node *Node) {
    next, prev := this.tail, this.tail.prev
    node.next, node.prev = next, prev
    next.prev = node
    prev.next = node
}

func (this *LRUCache) Get(key int) int {
    node, ok := this.cache[key]
    if ok {
        this.remove(node)
        this.insert(node)
        return node.val
    }
    return -1
}

func (this *LRUCache) Put(key int, value int) {
    node, ok := this.cache[key]
    if ok {
        this.remove(node)
    }
    this.cache[key] = NewNode(key,value)
    this.insert(this.cache[key])

    if len(this.cache) > this.capacity {
        lru := this.head.next
        this.remove(lru)
        delete( this.cache, lru.key )
    }
}
