'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
'''

# BFS 

'''
A first thought might be to determine the rules for placing parentheses.
We can place an open paren '(' if the amount of open parens so far is less than n. We can place a closing paren ')' if the amount of open parens is greater than the
amount of closed parens. 
With these rules in mind we are going to use a tuple to keep track of the following:
the valid parentheses string built so far tmp[0], the amount of open parens in this string tmp[1],
and the amount of closed parens tmp[2]. Now the way we start is by adding to the queue ('(', 1, 0),
corresponding to having a valid parentheses string '(' with one open paren and zero closed parens.
In the while loop we pop from the queue, if the valid parentheses string uses all of the pairs of parens we add it to the ans list.
Now, using our rules mentioned above, we place open and closing parens and add this new valid parentheses string to the queue to be processed.
'''

class Solution(object):
    def generateParenthesis(self, n):
        # BFS
        queue = [('(', 1, 0)]
        ans = []
        while queue:
            tmp = queue.pop(0)
            if len(tmp[0]) == 2*n:
                ans += [tmp[0]]
            if tmp[1] < n:
                queue += [(tmp[0] + '(', tmp[1] + 1, tmp[2])]
            if tmp[2] < tmp[1]:
                queue += [(tmp[0] + ')', tmp[1], tmp[2] + 1)]
        return ans
      
# BACKTRACKING

'''
 add '(' or ')' when we know it will remain a valid sequence. We can do this by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
'''

class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans
