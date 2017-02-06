# coding:utf-8

"""
12. Integer to Roman

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        number = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        result = ""
        x = 0
        for x in range(0, 13):
            while num >= number[x]:
                num -= number[x]
                result += roman[x]
            x += 1
        return result

def main():
    solution = Solution()
    print solution.intToRoman(21)
    print solution.intToRoman(99)
if __name__ == '__main__':
    main()