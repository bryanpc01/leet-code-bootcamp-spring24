## Had assistance from youtube and firends.

def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [[1,0], [-1,0],[0,1],[0,-1]]
    dp = {}

    def dfs(row, col, val):
        # terminating condition
        if (row < 0 or row == rows) or (col < 0 or col == cols) or matrix[row][col] <= val:
            return 0

        if (row,col) in dp:
            return dp[(row,col)]

        res = 1
        for d_row, d_col in directions:
            res = max(res, 1 + dfs(row + d_row, col + d_col, matrix[row][col]))

        dp[(row,col)] = res

        return res

    for row in range(rows):
        for col in range(cols):
            dfs(row,col,-1)

    return max(dp.values())
