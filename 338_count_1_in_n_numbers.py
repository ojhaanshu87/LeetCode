'''
Given an integer num, return an array of the number of 1's in the binary representation of every number in the range [0, num].

 

Example 1:
Input: num = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: num = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 
Constraints:

0 <= num <= 105
 

Follow up:

It is very easy to come up with a solution with run time O(32n). Can you do it in linear time O(n) and possibly in a single pass?
Could you solve it in O(n) space complexity?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''

# Division method
class Solution(object):
    def countBits(self, num):
        res=[0]
        for i in range(1, num + 1):
            if i % 2 == 0:
                res.append(res[i // 2])
            else:
                res.append(res[(i-1) // 2] + 1)
        return res


# Convert number to Binary then count 1's and append to list
class Solution(object):
    def decimal_to_binary_rec (self, num):
        return bin(num)
        
    def countBits(self, num):
        res = []
        for elem in range(0, num + 1):
            to_bin = self.decimal_to_binary_rec(elem)
            to_list = [x for x in to_bin]
            res.append(to_list.count('1'))
        return res
