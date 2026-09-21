class KeyVal:
    def __init__(self,key:int,val:int):
        self.key = key
        self.val = val

class HashTable:
    def __init__(self, capacity: int):
        self.arr = [None] * capacity
        self.cap = capacity
        self.size = 0
    
    def _hash(self,key:int) -> int:
        return key % self.cap

    def insert(self, key: int, value: int) -> None:
        i = self._hash(key)
        while True:
            if self.arr[i] == None:
                break
            elif self.arr[i].key == key:
                self.arr[i].val = value
                return
            i = self._hash(i+1)
        self.arr[i] = KeyVal(key,value)
        self.size += 1
        if self.size >= self.cap//2:
            self.resize()

    def get(self, key: int) -> int:
        i = self._hash(key)
        while self.arr[i]:
            if self.arr[i].key == key:
                return self.arr[i].val
            i = self._hash(i+1)
        return -1

    def remove(self, key: int) -> bool:
        i = self._hash(key)
        while self.arr[i]:
            if self.arr[i].key == key:
                self.size -= 1
                self.arr[i] = None
                return True
            i = self._hash(i+1)
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        self.cap *= 2
        arr = [None] * self.cap
        for i in range(len(self.arr)):
            arr[i] = self.arr[i]
        self.arr = arr