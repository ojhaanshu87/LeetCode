# You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. 
# You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

# Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

 

# Example 1:
# Input: s1 = "xx", s2 = "yy"
# Output: 1
# Explanation: 
# Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".

# Example 2: 
# Input: s1 = "xy", s2 = "yx"
# Output: 2
# Explanation: 
# Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
# Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
# Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.

# Example 3:
# Input: s1 = "xx", s2 = "xy"
# Output: -1

# Example 4:
# Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
# Output: 4

class Solution(object):
    def minimumSwap(self, s1, s2):
        xy, yx, result = 0, 0, 0
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
        # The divmod() method in python takes two numbers and returns a pair of numbers consisting of their quotient and remainder.
        # Input : x = 9, y = 3 OUTPUT (3, 0)
        xy_swaps, xy_rem = divmod(xy, 2)
        yx_swaps, yx_rem = divmod(yx, 2)
        
        if xy_rem == 1 or yx_rem == 1:
            return xy_swaps + yx_swaps + 2 if xy_rem == yx_rem else -1
        else:
            return xy_swaps + yx_swaps
