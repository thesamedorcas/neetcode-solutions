class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows= len(grid)
        cols= len(grid[0])


        if rows<=0:
            return 0
        if cols<=0:
            return 0

        def dfs(row, col):
            stack=[(row, col)]
            count=1
            while stack:
                curr, curc= stack.pop()

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    r, c= curr+dr, curc+dc
                    if 0<=r<rows and 0<=c<cols and grid[r][c] ==1:
                        count+=1
                        grid[r][c]= 0
                        stack.append((r, c))
            return count


        count=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    grid[r][c]=0
                    cur= dfs(r, c)
                    count= max(count, cur)

        return count