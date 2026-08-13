class Node:
    def __init__(self,val:int,prev = None,next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = Node(value,self.tail.prev,self.tail)
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = Node(value,self.head, self.head.next)
        self.head.next.prev = newNode
        self.head.next = newNode

    def pop(self) -> int:
        val = -1
        if not self.isEmpty():
            val = self.tail.prev.val
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
        return val

    def popleft(self) -> int:
        val = -1
        if not self.isEmpty():
            val = self.head.next.val
            self.head.next.next.prev = self.head
            self.head.next = self.head.next.next
        return val
        
