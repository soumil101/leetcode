class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
        # this is multi source bfs
        # find every treasure chest in first pass and add to queue
        # level by level bfs from each chest until you hit and mark every land 
        m = len(grid)
        n = len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        queue = deque()

        # first pass find every treasure chest coordinate
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    queue.append((r,c))

        # now we have every single treasure chest in our queue
        # now run source bfs (level order traversal)
        while queue:
            curr_r, curr_c = queue.popleft()
            # check every direction in bounds and check if the cell is land
            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[curr_r][curr_c] + 1
                    queue.append((nr, nc))