class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [int(0)] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size + 1 > self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size] 

    def resize(self) -> None:
        self.capacity *= 2
        arr = [0] * self.capacity
        for i,n in enumerate(self.arr):
            arr[i] = n
        self.arr = arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity