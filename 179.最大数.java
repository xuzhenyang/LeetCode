import java.util.Arrays;
import java.util.stream.Collectors;

/*
 * @lc app=leetcode.cn id=179 lang=java
 *
 * [179] 最大数
 */

// @lc code=start
/**
 * 思路
 * 使用java的sort方法，排序规则：两数左右换位，相加比较字典序
 */
class Solution {
    public String largestNumber(int[] nums) {
        String result = Arrays.stream(nums)
        .mapToObj(String::valueOf)
        .sorted((o1, o2) -> (o2 + o1).compareTo(o1 + o2))
        .collect(Collectors.joining());
        return result.charAt(0) == '0' ? "0" : result;
    }
}
// @lc code=end

