class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        numIslands = 0 
        
        # Create visited set:
        visited = set()
        
        # Get dimensions:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        # Create BFS:
        def BFS(r, c):
            # Base case - out of bounds, water reached, or visited:
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r, c) in visited:
                return
            
            # Add current cell to visited land:
            visited.add((r,c))
            
            # Perform BFS on neighboring cells:
            # Go left:
            BFS(r, c-1)
            # Go up:
            BFS(r-1, c)
            # Go right:
            BFS(r, c+1)
            # Go down:
            BFS(r+1, c)
        
        # Loop through grid:
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    numIslands += 1
                    BFS(r,c)
        
        return numIslands