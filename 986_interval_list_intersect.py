"""
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b. 
The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.
For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""

#ALGORITHM
#If A[0] has the smallest endpoint, it can only intersect B[0]. After, we can discard A[0] since it cannot intersect anything else.

#Similarly, if B[0] has the smallest endpoint, it can only intersect A[0], and we can discard B[0] after since it cannot intersect anything else.

#We use two pointers, i and j, to virtually manage "discarding" A[0] or B[0] repeatedly.

#Time Complexity: O(M + N)O(M+N), where M, NM,N are the lengths of A and B respectively.
#Space Complexity: O(M + N)O(M+N), the maximum size of the answer.

class Solution(object):
    def intervalIntersection(self, A, B):
        res, ptr_a, ptr_b = [], 0, 0
        while ptr_a < len(A) and ptr_b < len(B):
            start = max(A[ptr_a][0], B[ptr_b][0])
            end = min(A[ptr_a][1], B[ptr_b][1])
            if start <= end:
                res.append([start, end])
            #remove interval with smallest endpoint
            if A[ptr_a][1] < B[ptr_b][1]:
                ptr_a += 1
            else:
                ptr_b += 1
        return res
        

