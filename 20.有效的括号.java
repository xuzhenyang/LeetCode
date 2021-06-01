import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=20 lang=java
 *
 * [20] 有效的括号
 */

// @lc code=start
class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<Character, Character>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                stack.push(c);
            } else if (stack.isEmpty()) {
                return false;
            } else {
                if (!Objects.equals(map.get(stack.pop()), c)) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}
// @lc code=end
