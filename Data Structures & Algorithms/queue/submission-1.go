type Node struct {
    val int
    next *Node
    prev *Node
}

func NewNode(val int, prev, next *Node) *Node {
    return &Node { val : val, prev : prev, next : next }
}

type Deque struct {
    head *Node
    tail *Node
}


func NewDeque() *Deque {
    head := NewNode(0,nil,nil)
    tail := NewNode(0,nil,nil)
    tail.prev = head
    head.next = tail
    return &Deque { head:head, tail:tail }
}

func (d *Deque) IsEmpty() bool {
    return d.head.next == d.tail
}

func (d *Deque) Append(value int) {
    newNode := NewNode(value,d.tail.prev,d.tail)
    d.tail.prev.next = newNode
    d.tail.prev = newNode
}

func (d *Deque) AppendLeft(value int) {
    newNode := NewNode(value,d.head,d.head.next)
    d.head.next.prev = newNode
    d.head.next = newNode
}

func (d *Deque) Pop() int {
    var val int = -1
    if !d.IsEmpty() {
        val = d.tail.prev.val
        d.tail.prev.prev.next = d.tail
        d.tail.prev = d.tail.prev.prev
    }
    return val
}

func (d *Deque) PopLeft() int {
    var val int = -1
    if !d.IsEmpty() {
        val = d.head.next.val
        d.head.next.next.prev = d.head
        d.head.next = d.head.next.next
    }
    return val
}
