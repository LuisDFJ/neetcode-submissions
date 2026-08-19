class Pair:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = [None for _ in range(capacity)]
    
    def hash(self, key:int) -> None:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        idx = self.hash(key)
        while True:
            if self.map[idx] == None:
                self.map[idx] = Pair(key,value)
                self.size += 1
                if self.size >= self.capacity//2:
                    self.resize()
                break
            elif self.map[idx].key == key:
                self.map[idx].val = value
                break
            idx = (idx+1)%self.capacity

    def get(self, key: int) -> int:
        idx = self.hash(key)
        while self.map[idx] != None:
            if self.map[idx].key == key:
                return self.map[idx].val
            idx = (idx+1)%self.capacity
        return -1

    def remove(self, key: int) -> bool:
        idx = self.hash(key)
        while self.map[idx] != None:
            if self.map[idx].key == key:
                self.map[idx] = None
                self.size -= 1
                return True
            idx = (idx+1)%self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        oldMap = self.map
        self.map = [None for _ in range(self.capacity)]
        self.size = 0
        for pair in oldMap:
            if pair:
                self.insert(pair.key,pair.val)
