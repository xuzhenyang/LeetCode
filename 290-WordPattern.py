# coding:utf-8

"""
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_dict = {}
        str_array = str.split(' ')
        if len(pattern) != len(str_array):
            return False
        for index in range(len(pattern)):
            if pattern_dict.has_key(pattern[index]):
                if str_array[index] != pattern_dict[pattern[index]]:
                    return False
            else:
                # 如果值已经存在 例如case4
                if str_array[index] in pattern_dict.values():
                    return False
                pattern_dict[pattern[index]] = str_array[index]
        return True

def main():
    solution = Solution()
    print solution.wordPattern("abba", "dog cat cat dog")
    print solution.wordPattern("abba", "dog cat cat fish")
    print solution.wordPattern("aaaa", "dog cat cat dog")
    print solution.wordPattern("abba", "dog dog dog dog")
if __name__ == '__main__':
    main()