class Node:
    def __init__(self, val : int):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        # Skip first dummy node
        cur = self.head.next
        while cur:
            if index == 0:
                break
            index -= 1
            cur = cur.next
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        # If new node is tail
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        cur = self.head
        # Get node before target
        i = 0
        while i < index and cur:
            i += 1
            cur = cur.next
        
        # Removing Node ahead of cur
        if cur and cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        cur = self.head.next
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr

        
