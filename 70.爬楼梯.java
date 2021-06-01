/*
 * @lc app=leetcode.cn id=70 lang=java
 *
 * [70] 爬楼梯
 */

// @lc code=start
class Solution {
    public int climbStairs(int n) {
        if (n <= 2) {
            return n;
        }
        int[] climbs = new int[n + 1];
        climbs[0] = 1;
        climbs[1] = 1;
        for (int i = 2; i <= n; i++) {
            climbs[i] = climbs[i - 1] + climbs[i - 2];
        }
        return climbs[n];
    }
}
// @lc code=end

