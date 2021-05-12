'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime? 

Example 1:
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [0]
Output: 0

Example 3:
Input: nums = [2,4]
Output: 6

Example 4:
Input: nums = [8,10,2]
Output: 10

Example 5:
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
'''

# Trie Solution. O(N) TC and O(1) space
# O(N) TC and O(1) Space
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.val = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_into_trie(self, binary_str, num):
        curr = self.root
        for bit in binary_str:
            curr = curr.children[int(bit)]
        curr.val = num
    
    def search_number(self, binary_str_to_match, target_num):
        curr = self.root
        for bit in binary_str_to_match:
            d = int(bit)
            want = d ^ 1

            if want in curr.children:
                curr = curr.children[want]
            else:
                curr = curr.children[want ^ 1]
        return curr.val ^ target_num

class Solution(object):
    def findMaximumXOR(self, nums):
        trie = Trie()
        max_xor = float("-inf")
        for num in nums:
            # zfill for convert to binary and keep leading zero
            binary_str = bin(num)[2:].zfill(32)
            trie.insert_into_trie(binary_str, num)
            max_xor = max(max_xor, trie.search_number(binary_str, num))
        return max_xor
        
