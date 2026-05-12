class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # shortcut
        if len(edges) != n - 1:
            return False

        parent = list(range(n))
        
        # use union find
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # recursively point straight to root using compression
            return parent[x]

        def union(x, y):
            # set one roots parent to the other
            px, py = find(x), find(y)
            if px == py:
                return False  # already same component
            parent[py] = px  # attach one root to the other
            return True

        for u, v in edges:
            if not union(u, v):
                # not False = True, already in same component (cycle)
                return False
        
        return True