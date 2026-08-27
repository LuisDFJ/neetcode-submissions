class UnionFind:
    def __init__(self,n:int):
        self.parents = [ i for i in range(n) ]
        self.rank = [0] * n
    def find(self,x:int) -> int:
        curr = self.parents[x]
        while curr != self.parents[curr]:
            self.parents[curr] = self.parents[self.parents[curr]]
            curr = self.parents[curr]
        return curr
    def union(self,x:int,y:int) -> bool:
        a,b = self.find(x),self.find(y)
        if a == b: return False
        if self.rank[a] < self.rank[b]:
            self.parents[a] = b
        elif self.rank[a] > self.rank[b]:
            self.parents[b] = a
        else:
            self.parents[a] = b
            self.rank[b] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAcc:
                    uf.union(i,emailToAcc[email])
                else:
                    emailToAcc[email] = i
        emailGroup = defaultdict(list)
        for email,i in emailToAcc.items():
            root = uf.find(i)
            emailGroup[root].append(email)
        
        res = []
        for i,emails in emailGroup.items():
            name = accounts[i][0]
            res.append( [name] + emails )
        return res