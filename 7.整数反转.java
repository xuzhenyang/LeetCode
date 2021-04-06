/*
 * @lc app=leetcode.cn id=7 lang=java
 *
 * [7] 整数反转
 */

// @lc code=start
class Solution {
    public int reverse(int x) {
        int max = Integer.MAX_VALUE;
        int min = Integer.MIN_VALUE;
        int result = 0;
        while(x != 0) {
            int pop = x % 10;
            if (result > max / 10 || (result == max / 10 && pop > 7)) {
                return 0;
            }
            if (result < min / 10 || (result == min / 10 && pop < -8)) {
                return 0;
            }
            result = result * 10 + pop;
            x = x / 10;
        }
        return result;
    }
}
// @lc code=end

