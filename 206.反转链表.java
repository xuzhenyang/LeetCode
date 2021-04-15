/*
 * @lc app=leetcode.cn id=206 lang=java
 *
 * [206] 反转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    //使用递归
    public ListNode reverseList(ListNode head) {
        //出口
        if (head == null || head.next == null) {
            return head;
        }
        //压栈,递归进入末端，得到反转后的head
        ListNode newHead = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        //返回反转后的head
        return newHead;
    }

    //使用迭代
    public ListNode reverseList1(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        while(current != null) {
            ListNode tmp = current.next;
            current.next = prev;
            prev = current;
            current = tmp;
        }
        return prev;
    }
}
// @lc code=end

