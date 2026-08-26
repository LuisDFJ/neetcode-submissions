class Trie:
    def __init__(self):
        self.childs = {}
        self.isWord = False
        self.word = None
    def add(self,word:str):
        curr = self
        for c in word:
            if c not in curr.childs:
                curr.childs[c] = Trie()
            curr = curr.childs[c]
        curr.isWord = True
        curr.word = word

class Solution:
    def neighbors(self,i:int,j:int) -> Iterable[tuple[int,int]]:
        N,M = len(self.board), len(self.board[0])
        for n,m in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <= n < N and 0 <= m < M and (n,m) not in self.visit:
                yield n,m

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.visit = set()
        root = Trie()
        for word in words:
            root.add(word)
        
        res = set()
        def dfs(i:int,j:int,root:Trie):
            if board[i][j] not in root.childs: return

            self.visit.add((i,j))
            root = root.childs[board[i][j]]
            if root.isWord:
                res.add(root.word)
            
            for n,m in self.neighbors(i,j):
                dfs(n,m,root)
            self.visit.remove((i,j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i,j,root)
        return list(res)




            
        