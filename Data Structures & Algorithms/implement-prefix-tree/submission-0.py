class Node:
    def __init__(self):
        self.childs = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childs:
                curr.childs[c] = Node()
            curr = curr.childs[c]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.childs:
                return False
            curr = curr.childs[c]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.childs:
                return False
            curr = curr.childs[c]
        return True
        
        