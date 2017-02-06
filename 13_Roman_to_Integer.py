# coding:utf-8

"""
13. Roman to Integer

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I" : 1,
            "X" : 10,
            "C" : 100,
            "M" : 1000,
            "V" : 5,
            "L" : 50,
            "D" : 500
        }
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
                result -= roman_dict[s[i]]
            else :
                result += roman_dict[s[i]]
        return result


def main():
    solution = Solution()
    print solution.romanToInt("MCMLXXX")
    print solution.romanToInt("XIX")
if __name__ == '__main__':
    main()