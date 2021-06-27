'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6
'''

class Solution(object):
    def uniquePaths(self, m, n):
        dp_table = [[1] * n for _ in range(m)]
        for col in range(1, m):
            for row in range(1, n):
                dp_table[col][row] = dp_table[col - 1][row] + dp_table[col][row - 1]
        return dp_table[m - 1][n - 1]
