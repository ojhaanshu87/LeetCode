'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Input: text = "nlaebolko"
Output: 1

Input: text = "loonbalxballpoon"
Output: 2
'''

class Solution(object):
    def maxNumberOfBalloons(self, text):
        temp = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for char in text:
            if char in temp:
                temp[char] += 1
                
        for k,v in temp.items():
            if k == 'l' or k == 'o':
                temp[k] //= 2
        return min(temp.values())
        
        # SHORT APPROACH
        # if not text:
        #     return 0
        # text_counter, balloon_counter = Counter(text), Counter('balloon')
        # return min(text_counter[k] // balloon_counter[k] for k in 'balon')
        
