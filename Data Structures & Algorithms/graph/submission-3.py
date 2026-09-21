class Graph:
    def __init__(self):
        self.adj = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj:
            self.adj[src] = set()
        if dst not in self.adj:
            self.adj[dst] = set()
        self.adj[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if (
            src not in self.adj or
            dst not in self.adj or
            dst not in self.adj[src]
        ): return False
        self.adj[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        queue = deque([src])
        visit = set([src])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == dst: return True
                for neighbor in self.adj[node]:
                    if neighbor not in visit:
                        visit.add(neighbor)
                        queue.append(neighbor)
        return False
        

