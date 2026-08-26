class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = {i:i for i in range(1,n+1)}
        rank = {i:0 for i in range(1,n+1)}

        def find( x : int ) -> int:
            curr = parents[x]
            while curr != parents[curr]:
                parents[curr] = parents[parents[curr]]
                curr = parents[curr]
            return curr
        
        def union( x : int, y : int ) -> bool:
            a,b = find(x),find(y)
            if a == b: return False
            if rank[a] > rank[b]:
                parents[b] = a
            elif rank[a] < rank[b]:
                parents[a] = b
            else:
                parents[a] = b
                rank[b] += 1
            return True
        
        for edge in edges:
            if not union(edge[0],edge[1]):
                return edge
        return []

        