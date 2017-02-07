# coding:utf-8

"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

先找到最短的字符串
遍历该字符串内字符 与其他字符串同位置字符一一比较 直到有个不一样的 index-1
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        length = len(strs[0])
        index = 0
        num = 0
        for i in range(len(strs)):
            if length > len(strs[i]):
                length = len(strs[i])
                index = i
        for i in range(len(strs[index])):
            for j in range(len(strs)):
                # print "i:%d j:%d" % (i,j)
                if strs[j][i] != strs[index][i]:
                    num = i - 1
                    return strs[index][0:num+1:]
                num = i
        return strs[index][0:num+1:]
        

def main():
    solution = Solution()
    strs = ["att"]
    print solution.longestCommonPrefix(strs)
    strs = ["att", "atdsfdf", "atttadsfad"]
    print solution.longestCommonPrefix(strs)
    strs = ["flower","flow","flight"]
    print solution.longestCommonPrefix(strs)
    strs = ["c","c","c"]
    print solution.longestCommonPrefix(strs)

if __name__ == '__main__':
    main()