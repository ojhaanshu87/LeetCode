'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
Example 4:

Input: s = "words and 987"
Output: 0
Explanation:
Step 1: "words and 987" (no characters read because there is no leading whitespace)
         ^
Step 2: "words and 987" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "words and 987" (reading stops immediately because there is a non-digit 'w')
         ^
The parsed integer is 0 because no digits were read.
Since 0 is in the range [-231, 231 - 1], the final result is 0.
Example 5:

Input: s = "-91283472332"
Output: -2147483648
Explanation:
Step 1: "-91283472332" (no characters read because there is no leading whitespace)
         ^
Step 2: "-91283472332" ('-' is read, so the result should be negative)
          ^
Step 3: "-91283472332" ("91283472332" is read in)
                     ^
The parsed integer is -91283472332.
Since -91283472332 is less than the lower bound of the range [-231, 231 - 1], the final result is clamped to -231 = -2147483648.
'''

# Approach 

# A) Remove preceding zeros;
# B) Determine the sign;
# C) Handle overflow;
# D) Deal with invalid inputs.

# For step 1, we can use built-in function str.lstrip() to finish, but note that unlike trim() in JAVA. Cos str.lstrip() just creates another string instead of changing the original one. That's why we have str = str.lstrip();

# For step 2, straight-forward idea;

# For step 3, well, in Python 3 or above, there is no limit on Integer(we don't need care about this if the testcase is Python-specific); However, by convention, we still need to handle it. I guess the code tells everything.

# For step 4, the most-upvoted solution seems not to care about length of the 'stripped' str; In my code, every time you increment i, you need to check whether it is still in the range. In this way, invalid inputs are handled quite efficiently and smartly.

class Solution(object):
    def myAtoi(self, s):
        i = 0; sign = 1; base = 0
        str_trim = s.lstrip()
        MAX_INT, MIN_INT  = 2147483647, -2147483648
        if i < len(str_trim) and (str_trim[i] == '+' or str_trim[i] == '-'):
            sign = 1 - 2 * (str_trim[i] == '-')
            i += 1
        while i < len(str_trim) and str_trim[i] >= '0' and str_trim[i] <= '9':
            if base > int(MAX_INT / 10) or (base == int(MAX_INT / 10) and ord(str_trim[i]) - ord('0') > 7):
                return MAX_INT if sign == 1 else MIN_INT
            base = base * 10 + int(str_trim[i])
            i += 1
        return base * sign
