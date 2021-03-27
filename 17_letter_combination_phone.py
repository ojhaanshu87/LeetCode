'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
'''
class Solution(object):
    def letterCombinations(self, digits):
        if digits == "":
            return []
        graph = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        
        """ Turn digits in to list of char list """
        chars = []
        for c in digits:
            chars.append(graph[c])
        """ Start with "" to concatenate """
        ans = [""]
        for i in range(len(chars)):
            ans=[c + chars[i][j] for c in ans for j in range(len(chars[i]))]   
        return ans
        
# DFS Solution TC - O(max_val_len_hash_map ^ len(digit)  * N) and Space (O(N))

class Solution(object):
    def letterCombinations(self, digits):
        res = []
        if not digits:
            return []
        temp_dict = {"2":"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
        self.dfs(temp_dict, digits, "", res)
        return res
    
    def dfs(self, temp_dict, digits, path, res):
        if not digits:
            res.append(path)
            return 
        for char in temp_dict[digits[0]]:
            self.dfs(temp_dict, digits[1:], path + char, res)
