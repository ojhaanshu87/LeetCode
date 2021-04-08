'''
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
'''

# Using Stack O(N) TC and O(N) Space
class Solution(object):
    def isRobotBounded(self, instructions):
        instructions += 3 * instructions
        list_dir, counter, stack = ['r','u','l','d'], 0, []
        for direction in instructions:
            if direction == 'G':
                stack.append(list_dir[counter % 4])
            elif direction == 'L':
                counter += 1
            else:
                counter -= 1
        temp_map = collections.Counter(stack)
        return temp_map['r'] == temp_map['l'] and temp_map['u'] == temp_map['d']
        
        


# O(N) TC and O(1) Space
class Solution(object):
    def isRobotBounded(self, instructions):
        # N, E, S, W = 0, 1, 2, 3
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        centre_x, centre_y = 0, 0
        #facing North
        idx = 0
        for direction in instructions:
            if direction == "L":
                idx = (idx + 3) % 4
            elif direction == "R":
                idx = (idx + 1) % 4
            else:
                centre_x += directions[idx][0]
                centre_y += directions[idx][1]
        # after one cycle either robot return to initial or doesnot face north
        return (centre_x == 0 and centre_y == 0) or idx != 0
        
 
