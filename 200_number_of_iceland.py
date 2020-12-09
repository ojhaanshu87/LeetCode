"""
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

#Time complexity : O(M \times N)O(M×N) where MM is the number of rows and NN is the number of columns.
#Space complexity : worst case O(M \times N)O(M×N) in case that the grid map is filled with lands where DFS goes by M \times NM×N deep


class Solution(object):
    def dfs(self, i, j, grid):
        # Breaking condition for recursive call
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        # Change the "1" found at i, j to "0" so that next time some recursive call reaches this point, we dont perform the same thing again
        grid[i][j] = "0"
        # Note this line in the question: "An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically", 
        #so we need to go in the basic 4 directions. There are many ways to do this, like using yield. But now, lets use the most common and simple way
        self.dfs(i + 1, j, grid)
        self.dfs(i - 1, j, grid)
        self.dfs(i, j + 1, grid)
        self.dfs(i, j - 1, grid)
    
    def numIslands(self, grid):
        res = 0
        if not grid:
            return res
        if len(grid) == 0 and len(grid[0]) == 0:
            return res
        for elem in range(len(grid)):
            for elem1 in range(len(grid[0])):
                if grid[elem][elem1] == "1":
                    self.dfs(elem, elem1, grid)
                    res += 1
        return res
        
