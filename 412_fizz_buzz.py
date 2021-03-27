'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''

# HashMap TC (O(N)) Space O(1)

class Solution(object):
    def fizzBuzz(self, n):
        res = []
        map_fizz_buzz = {3 : "Fizz", 5 : "Buzz"}

        for elem in range(1, n + 1):
            elem_str = ''
            for key in map_fizz_buzz.keys():
                if elem % key == 0:
                    elem_str += map_fizz_buzz[key]
            if not elem_str:
                elem_str = str(elem)
            res.append(elem_str)
        return res
        
