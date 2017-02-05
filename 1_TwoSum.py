# coding:utf-8

"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # low
        # for first in range(len(nums)):
        #     for second in range(first + 1, len(nums)):
        #         if nums[first] + nums[second] == target:
        #             print '%d %d' % (nums[first], nums[second])
        #             return [first, second]

        # high
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i


def main():
    nums = [3,2,4]
    target = 6
    solution = Solution()
    print solution.twoSum(nums, target)

if __name__ == '__main__':
    main()