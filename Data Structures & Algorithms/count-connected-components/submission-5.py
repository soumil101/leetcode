class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            parent[ry] = rx  # attach root of y to root of x
            return True

        for u, v in edges:
            union(u, v)

        # Optional: compress paths for all nodes
        for i in range(n):
            find(i)

        # Count distinct roots
        return len({find(i) for i in range(n)})