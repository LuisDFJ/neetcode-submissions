class Node:
    def __init__(self,val:int,next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        while curr:
            if index == 0: return curr.val
            index -= 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        self.head.next = Node(val,self.head.next)
        if self.tail == self.head:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        while curr.next:
            if index == 0:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                return True
            index -= 1
            curr = curr.next
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res