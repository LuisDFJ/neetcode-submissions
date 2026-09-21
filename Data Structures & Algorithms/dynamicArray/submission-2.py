class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.cap = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.cap == self.size:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        self.arr[self.size], val = 0, self.arr[self.size]
        return val

    def resize(self) -> None:
        self.cap *= 2
        arr = [0] * self.cap
        for i in range(self.size):
            arr[i] = self.arr[i]
        self.arr = arr

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.cap