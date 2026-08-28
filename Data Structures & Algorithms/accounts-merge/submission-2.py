class UnionFind:
    def __init__(self,n:int):
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]
    def find(self, x : int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x
    def union(self,x:int,y:int) -> bool:
        a,b = self.find(x), self.find(y)
        if a == b: return False
        if self.ranks[a] > self.ranks[b]:
            self.parents[b] = a
        elif self.ranks[a] < self.ranks[b]:
            self.parents[a] = b
        else:
            self.parents[a] = b
            self.ranks[b] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAccount = {}
        for id,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToAccount:
                    uf.union(id,emailToAccount[email])
                else:
                    emailToAccount[email] = id
        
        emailGroup = defaultdict(list)
        for email,id in emailToAccount.items():
            root = uf.find(id)
            emailGroup[root].append(email)
        return [ [accounts[id][0]] + group for id, group in emailGroup.items() ]

        
        