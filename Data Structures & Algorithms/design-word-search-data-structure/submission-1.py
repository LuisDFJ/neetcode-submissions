class Node:
    def __init__(self):
        self.childs = {}
        self.word = False
class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.childs:
                curr.childs[c] = Node()
            curr = curr.childs[c]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(root: Node, i: int) -> bool:
            if i == len(word): return root.word
            if word[i] == ".":
                for c in root.childs:
                    if dfs(root.childs[c],i+1):
                        return True
            else:
                if word[i] in root.childs:
                    return dfs(root.childs[word[i]],i+1)
            return False
        return dfs(self.root,0)
            
        
