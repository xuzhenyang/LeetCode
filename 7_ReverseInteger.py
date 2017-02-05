# coding:utf-8

"""
7. Reverse Integer

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(abs(x))
        result = string[::-1]
        if int(result) > 2147483647:
            return 0
        if x >= 0:
            return int(result)
        else:
            return -1 * int(result)

def main():
    solution = Solution()
    print solution.reverse(1534236469)
if __name__ == '__main__':
    main()