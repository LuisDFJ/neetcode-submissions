"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        graph = {}
        def dfs(root: Node) -> Node:
            if root in graph:
                return graph[root]
            
            graph[root] = Node(root.val)
            for neighbor in root.neighbors:
                graph[root].neighbors.append(dfs(neighbor))
            return graph[root]
        
        return dfs(node)