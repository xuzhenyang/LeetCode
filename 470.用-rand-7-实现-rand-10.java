/*
 * @lc app=leetcode.cn id=470 lang=java
 *
 * [470] 用 Rand7() 实现 Rand10()
 */

// @lc code=start
/**
 * The rand7() API is already defined in the parent class SolBase.
 * public int rand7();
 * @return a random integer in the range 1 to 7
 */
/**
 * 思路
 * 随机函数直接相加会导致概率不均匀，使用乘法升维度
 * (rand7() - 1) * 7 + rand7() 得到rand49，即 [1,49]的均匀随机
 * 对于大于40的数，使用拒绝采样，重新rand
 * [1,40]内的数，通过 rand10*N() % 10 + 1 来获得 rand10()
 */
class Solution extends SolBase {
    public int rand10() {
        while (true) {
            int result = (rand7() - 1) * 7 + rand7();
            if (result <= 40) {
                return result % 10 + 1;
            }
        }
    }
}
// @lc code=end

