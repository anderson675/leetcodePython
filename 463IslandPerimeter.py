class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output = 0
        n, m = len(grid), len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    output+=4
                    if r > 0 and grid[r-1][c]: output-=2
                    if c > 0 and grid[r][c-1]: output-=2
                        
        return output