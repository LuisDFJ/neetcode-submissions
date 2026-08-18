class Node:
    def __init__(self,key :int, val :int) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertEnd(self, node : Node) -> None:
        prv,nxt = self.tail.prev, self.tail
        prv.next = nxt.prev = node
        node.next, node.prev = nxt,prv
    
    def remove(self, node : Node) -> None:
        nxt,prv = node.next, node.prev
        nxt.prev, prv.next = prv,nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insertEnd(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key,value)
        self.cache[key] = node
        self.insertEnd(node)
        
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            self.cache.pop(lru.key)
        
