class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows= len(grid)
        cols= len(grid[0])

        if rows==0:
            return 0
        if cols==0:
            return 0

        def dfs(sr, sc):
            stack= [(sr, sc)]

            while stack:
                curr, curc= stack.pop()

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    r, c= curr+dr, curc+dc

                    if 0<=r<rows and 0<=c<cols and grid[r][c] =="1":
                        stack.append((r, c))
                        grid[r][c]="0"

        count=0
        for r in range (rows):
            for c in range (cols):
                if grid[r][c]=="1":
                    grid[r][c]="0"
                    dfs(r, c)
                    count+=1

        return count


        