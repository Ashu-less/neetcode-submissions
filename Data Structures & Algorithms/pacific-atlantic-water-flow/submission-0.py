class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set() # lcoaitons taht can reach both pacific and atl positons
        def dfs(r, c, visited, prevHeight): # prevHeight we want to be smaller(closer to edge) because water flows to ocean large to small
            if(r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or heights[r][c] < prevHeight):
                return
            

            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c]) 
            dfs(r, c - 1, visited, heights[r][c])#current height is put as prev
            dfs(r, c + 1, visited, heights[r][c])


        

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows-1][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        return list(pac & atl)