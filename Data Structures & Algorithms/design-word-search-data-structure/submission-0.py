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
        def dfs(root: Node, word: str) -> bool:
            if not word: return root.word
            if word[0] == ".":
                for c in root.childs:
                    if dfs(root.childs[c],word[1:]):
                        return True
            else:
                if word[0] in root.childs:
                    return dfs(root.childs[word[0]],word[1:])
            return False
        return dfs(self.root,word)
            
        
