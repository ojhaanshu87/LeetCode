"""
Convert a non-negative integer num to its English words representation.

 

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution(object):
    def numberToWords(self, num):
        def convert(n):
            units_words = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
            tens_words = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
            teens_words = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
            
            n, units = divmod(n, 10)            
            n, tens = divmod(n, 10)
            hundreds = n
            
            s = ""
            if hundreds:
                s += units_words[hundreds] + " Hundred"
                
            if tens == 1 and units > 0:
                s += (" " if s else "") + teens_words[units]
            else:
                if tens:
                    s += (" " if s else "") + tens_words[tens]
                if units:
                    s += (" " if s else "") + units_words[units]
                    
            return s
        
        result = ""
        powers = [(10**9, ' Billion'), (10**6, ' Million'), (10**3, ' Thousand'), (1, '')]        
        for power, word in powers:
            triad = (num // power) % 10**3
            if triad:
                result += (" " if result else "") + convert(triad) + word
        
        return result or 'Zero'
        
