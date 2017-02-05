# coding:utf-8

"""
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
"""
1     7   2n-2
2   6 8   2n-2-2*i
3 5   9
4     10

1   5
2 4 6
3   7
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows < 2):
            return s
        result = ''
        length = len(s)
        cycle = 2 * numRows - 2
        for i in range(numRows):
            j = i
            while j < length:
                result += s[j]
                if (i > 0 and i < numRows - 1):
                    t = j
                    cycle2 = cycle - 2 * i
                    t += cycle2
                    if (t < length):
                        result += s[t]
                j += cycle
        return result
            


def main():
    solution = Solution()
    print solution.convert("PAYPALISHIRING", 3)
if __name__ == '__main__':
    main()