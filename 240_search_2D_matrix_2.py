```
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
```
#Algorithm Time complexity : O(lg(n!))  Space O(1)
```
First, we ensure that matrix is not null and not empty. 
Then, if we iterate over the matrix diagonals, we can maintain an invariant that the slice of the row and column beginning at the current (row, col)(row,col) pair is sorted.
Therefore, we can always binary search these row and column slices for target.
We proceed in a logical fashion, iterating over the diagonals, binary searching the rows and columns until we either run out of diagonals (meaning we can return False) or
find target (meaning we can return True).
The binarySearch function works just like normal binary search, but is made ugly by the need to search both rows and columns of a two-dimensional array.```

class Solution(object):
    def search_driver(self, matrix, target, start, columnwise):
        low = start
        high = len(matrix[0])-1 if columnwise else len(matrix)-1

        while low <= high:
            mid = (low + high)//2
            if columnwise:
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid - 1
                else:
                    return True
            else: # searching a row
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid - 1
                else:
                    return True
        
        return False

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.search_driver(matrix, target, i, True)
            horizontal_found = self.search_driver(matrix, target, i, False)
            if vertical_found or horizontal_found:
                return True
        
        return False
