'''
#200 Number of Islands Solution

By Joseph Haenel

12/21/2023

LeetCode Difficulty: Medium

m = numRows and n = numCols
Time Complexity is O(mn) 
Space Complexity is O(mn)
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        stack = list()

        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    stack.append((row, col))
                    grid[row][col] = "0"
                    while stack:
                        x, y = stack.pop()
                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            newX, newY = x + dx, y + dy
                            if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == "1":
                                stack.append((newX, newY))
                                grid[newX][newY] = "0"
        return islands


        