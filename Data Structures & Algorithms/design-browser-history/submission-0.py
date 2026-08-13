class Node:
    def __init__(self, url: str,prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node("")
        self.tail = Node("")
        self.cur  = Node(homepage, self.head, self.tail)
        self.head.next = self.tail.prev = self.cur

    def visit(self, url: str) -> None:
        self.cur.next = Node(url,self.cur,self.tail)
        self.cur = self.cur.next
        self.tail.prev = self.cur

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.prev == self.head: break
            self.cur = self.cur.prev
        return self.cur.url

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.next == self.tail: break
            self.cur = self.cur.next
        return self.cur.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)