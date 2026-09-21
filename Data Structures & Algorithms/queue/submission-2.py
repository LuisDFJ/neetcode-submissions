class Node:
    def __init__(self,val:int,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next,self.tail.prev = self.tail,self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        prev = self.tail.prev
        self.tail.prev = Node(value,self.tail,self.tail.prev)
        prev.next = self.tail.prev

    def appendleft(self, value: int) -> None:
        next = self.head.next
        self.head.next = Node(value,self.head.next,self.head)
        next.prev = self.head.next

    def pop(self) -> int:
        if not self.tail.prev.prev: return -1
        node = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return node.val

    def popleft(self) -> int:
        if not self.head.next.next: return -1
        node = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return node.val