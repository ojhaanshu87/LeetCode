```
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
```
```
The approach is basically the same as for quicksort.
For simplicity let's notice that kth largest element is the same as N - kth smallest element, hence one could implement kth smallest algorithm for this problem.


First one chooses a pivot, and defines its position in a sorted array in a linear time. This could be done with the help of partition algorithm.

To implement partition one moves along an array, compares each element with a pivot, and moves all elements smaller than pivot to the left of the pivot.

As an output we have an array where pivot is on its perfect position in the ascending sorted array,
all elements on the left of the pivot are smaller than pivot, and all elements on the right of the pivot are larger or equal to pivot.

Hence the array is now split into two parts. If that would be a quicksort algorithm, 
one would proceed recursively to use quicksort for the both parts that would result in O(NlogN) time complexity.
Here there is no need to deal with both parts since now one knows in which part to search for N - kth smallest element,
and that reduces average time complexity to O(N).

Finally the overall algorithm is quite straightforward :

Choose a random pivot.

Use a partition algorithm to place the pivot into its perfect position pos in the sorted array,
move smaller elements to the left of pivot, and larger or equal ones - to the right.
Compare pos and N - k to choose the side of array to proceed recursively. ```


class Solution(object):
    def swap(self, array, start, end):
        array[start], array[end] = array[end], array[start]
        
    def partition(self, array, start, end):
        pivot = start
        for elem in range (start + 1, end + 1):
            if array[elem] <= array[start]:
                pivot += 1
                self.swap(array, elem, pivot)
        self.swap(array, pivot, start)
        return pivot
    
    def findKthLargest(self, nums, k):
        # nums.sort()
        # reverse_nums = nums[::-1]
        # return reverse_nums[k-1]
        
        target_idx = len(nums) - k
        pivot, start, end = -1, 0, len(nums) - 1
        while pivot != target_idx:
            pivot = self.partition(nums, start, end)
            if pivot > target_idx:
                end = pivot - 1
            elif pivot < target_idx:
                start = pivot + 1
        return nums[pivot]
        
        
