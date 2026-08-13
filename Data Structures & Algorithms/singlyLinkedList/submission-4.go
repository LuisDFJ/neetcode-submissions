type Node struct {
    val int
    next *Node
}

func NewNode( val int, next *Node ) *Node {
    return &Node{val:val, next:next}
}

type LinkedList struct {
    head *Node
    tail *Node
}

func NewLinkedList() *LinkedList {
    head := NewNode(-1,nil)
    return &LinkedList {
        head:head,
        tail:head,
    }
}

func (ll *LinkedList) Get(index int) int {
    cur := ll.head.next
    i := 0
    for cur != nil {
        if i == index { break }
        i += 1
        cur = cur.next
    }
    if cur == nil { return -1 }
    return cur.val
}

func (ll *LinkedList) InsertHead(val int) {
    isTail := ll.head.next == nil
    newNode := NewNode(val,ll.head.next)
    ll.head.next = newNode
    if isTail {
        ll.tail = newNode
    }
}

func (ll *LinkedList) InsertTail(val int) {
    ll.tail.next = NewNode(val,nil)
    ll.tail = ll.tail.next
}

func (ll *LinkedList) Remove(index int) bool {
    var cur, prev *Node = ll.head.next, ll.head
    i := 0
    // Find the (i-1)th node
    for cur != nil {
        if i == index { break }
        i += 1
        prev = cur
        cur = cur.next
    }

    // Out of range detection
    if prev.next == nil {
        return false
    }
    // Remove current node by linking prev with cur.next
    prev.next = cur.next
    // If removing tail, link tail to the new end
    if cur == ll.tail { ll.tail = prev }
    return true
}

func (ll *LinkedList) GetValues() []int {
    var arr []int = make([]int,0)
    cur := ll.head.next
    for cur != nil {
        arr = append(arr,cur.val)
        cur = cur.next
    }
    return arr
}
