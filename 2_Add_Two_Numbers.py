# coding:utf-8

"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = ListNode(0)
        flag = 0
        head = tmp
        while l1 or l2 or flag:
            if l1:
                tmp.val += l1.val
                l1 = l1.next
            if l2:
                tmp.val += l2.val
                l2 = l2.next
            flag = tmp.val / 10
            tmp.val %= 10
            tmp.next = ListNode(flag)
            tmp = tmp.next
        tmp = head
        while tmp:
            if tmp.next.next == None:
                tmp.next = None
                break
            tmp = tmp.next
        return head

def main():
    """
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)
    l1_2.next = l1_3
    l1_1.next = l1_2
    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)
    l2_2.next = l2_3
    l2_1.next = l2_2
    """
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print result.val
        result = result.next
    l1 = ListNode(5)
    l2 = ListNode(5)
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print result.val
        result = result.next

if __name__ == '__main__':
    main()