```
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
```

#Algorithm
``` The algorithm is a standard binary search :
          
          Initialise left and right indexes left = 0 and right = m x n - 1.
          while left < right :
                Pick up the index in the middle of the virtual array as a pivot index : pivot_idx = (left + right) / 2.
                
                The index corresponds to row = pivot_idx // n and col = pivot_idx % n in the initial matrix,
                and hence one could get the pivot_element. This element splits the virtual array in two parts.
                
                Compare pivot_element and target to identify in which part one has to look for target. ```

class Solution(object):
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        start, end = 0, m * n - 1
        while start <= end:
                pivot_idx = (start + end) // 2
                pivot_elem = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_elem:
                    return True
                else:
                    if target < pivot_elem:
                        end = pivot_idx - 1
                    else:
                        start = pivot_idx + 1
        return False
