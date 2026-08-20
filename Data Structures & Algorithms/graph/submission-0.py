from collections import deque
class Graph:
    def __init__(self):
        self.adjList = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = []
        if dst not in self.adjList:
            self.adjList[dst] = []
        self.adjList[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjList or dst not in self.adjList or dst not in self.adjList[src]:
            return False
        self.adjList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        queue = deque([src])
        visit = set([src])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == dst:
                    return True
                for n in self.adjList.get(node,[]):
                    visit.add(n)
                    queue.append(n)
        return False

