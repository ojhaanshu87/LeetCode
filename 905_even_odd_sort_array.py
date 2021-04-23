'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''

# Single Paas, 2 Pointer, O(N) time, O(1) Space

'''
We'll maintain two pointers i and j. The loop invariant is everything below i has parity 0 (ie. A[k] % 2 == 0 when k < i), and everything above j has parity 1.

Then, there are 4 cases for (A[i] % 2, A[j] % 2):

If it is (0, 1), then everything is correct: i++ and j--.

If it is (1, 0), we swap them so they are correct, then continue.

If it is (0, 0), only the i place is correct, so we i++ and continue.

If it is (1, 1), only the j place is correct, so we j-- and continue.

Throughout all 4 cases, the loop invariant is maintained, and j-i is getting smaller. So eventually we will be done with the array sorted as desired.
'''

class Solution(object):
    def sortArrayByParity(self, A):
        start, end = 0, len(A) - 1
        while start < end:
            if A[start] % 2 > A[end] % 2:
                A[start], A[end] = A[end], A[start]
            if A[start] % 2 == 0:
                start += 1
            if A[end] % 2 == 1:
                end -= 1
        return A
      
      

# Brute Force, Two Paas
class Solution(object):
    def sortArrayByParity(self, A):
        odd_elem = [elem for elem in A if elem % 2 != 0]
        for elem in odd_elem:
            A.remove(elem)
            A.append(elem)
        return A
