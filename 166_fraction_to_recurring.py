'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"

Example 4:
Input: numerator = 4, denominator = 333
Output: "0.(012)"

Example 5:
Input: numerator = 1, denominator = 5
Output: "0.2"
'''

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        '''
        1. If numerator is divisible by denominator, return the string format of numerator/denominator
        2. Else, first check if the signs of the numerator and the denominator is opposite. If they are opposite, set the result string initially as "-"
        3. Take the absolute values of numerator and denominator
        4. Now while the remainder of numerator/denominator>0, add string of integer division (numerator*10)/denominator to result string. 
        In each iteration set numerator=numerator%denominator.
        5. Check whether any remainder has been appeared before. Use a map/dictionary to store the occurrence position of each remainder value
        6. If any remainder value x has been previously found at index i, then insert "(" in index i-1 of the string and add ")" at
        the end of the string and return the string
        '''
        
        if numerator%denominator==0:                                        
            return str(numerator//denominator)                             
        
        result=""  #stores the integer part
        if numerator<0 and denominator>0 or numerator>0 and denominator<0:
            result+="-"  #signs are opposite, add "-" to result string
        
        numerator = abs(numerator)
        denominator=abs(denominator) #take absolute of both values
            
        result+=str(numerator//denominator)+"." #add integer part to the result string and a decimal sign
        decimal = ""
        remainders = {}  #stores all the remainder occurrences
        k=0   #for getting the occurrence position of a remainder
        repeat_index = -1  #the index where any repeating remainder has first appeared         
        
        while numerator>0:
            k+=1                                                            
            numerator%=denominator #in each step set numerator as the remainder of numerator/denominator
            if numerator in remainders.keys():
                repeat_index=remainders[numerator]  #occurred before, get the first occurrence from the dictionary
                decimal=decimal[0:repeat_index-1]+"("+decimal[repeat_index-1:]+")"  #add "(" at the first occurrence and ")" at the end
                break
            if numerator==0:
                break  #remainder is divisible by denominator, don't need to check further
            remainders[numerator] = k #add the index of the remainder occurrence to dict
            numerator *= 10  #in each step numerator should be 10 times the remainder
            decimal+=str(numerator//denominator) #add string representation of the division to the string representation decimal portion
            
        return result+decimal
        
