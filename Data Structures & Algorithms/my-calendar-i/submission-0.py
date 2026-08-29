class Node:
    def __init__(self, start:int,end:int) -> None:
        self.left = None
        self.right = None
        self.start = start
        self.end = end
    def add(self,start:int,end:int) -> bool:
        if start >= self.end:
            if not self.right:
                self.right = Node(start,end)
                return True
            return self.right.add(start,end)
        elif end <= self.start:
            if not self.left:
                self.left = Node(start,end)
                return True
            return self.left.add(start,end)
        else:
            return False

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = Node(startTime,endTime)
            return True
        else:
            return self.root.add(startTime,endTime)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)