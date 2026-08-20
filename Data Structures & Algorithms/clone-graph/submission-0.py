"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        newGraph = {}
        newGraph[node] = Node(node.val)
        queue = deque([node])

        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in newGraph:
                    newGraph[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                newGraph[n].neighbors.append(newGraph[neighbor])
        return newGraph[node]



        