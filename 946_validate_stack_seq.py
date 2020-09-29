```
Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence
of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
```

#APPROACH -> GREEDY -> Time and Space O(N) where N is len(push or pop)

  #For each value, push it to the stack.

  #Then, greedily pop values from the stack if they are the next values to pop.

  #At the end, we check if we have popped all the values successfully.
  

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        count, stack = 0, []
        for elem in pushed:
            stack.append(elem)
            while stack and count < len(popped) and stack[-1] == popped[count]:
                stack.pop()
                count += 1
        return count == len(popped)
        
