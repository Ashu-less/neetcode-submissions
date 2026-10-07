class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows, cols = len(image), len(image[0])
        #visited = set() we dont need a visited bc we itearte through and change, so no need
        oldColor = image[sr][sc]
        if oldColor == color:
            return image
        def dfs(r, c, oldColor, newColor):
            if(r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] == newColor or image[r][c] != oldColor):
                return False
            image[r][c] = newColor
            dfs(r - 1, c, oldColor, newColor)
            dfs(r + 1, c, oldColor, newColor)
            dfs(r, c - 1, oldColor, newColor)
            dfs(r, c + 1, oldColor, newColor)

        dfs(sr, sc, oldColor, color)
        return image


        