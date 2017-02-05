# coding:utf-8

"""
9. Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        base = 1
        while x / base >= 10:
            base *= 10
        while x != 0:
            left = x / base
            right = x % 10
            if left != right:
                return False
            x -= left * base
            x /= 10
            base /= 100
        return True


def main():
    solution = Solution()
    print solution.isPalindrome(1001)
    print solution.isPalindrome(1023201)
if __name__ == '__main__':
    main()

"""
        int digits = 0;  
        int t = x;  
        int d = 0;  
        while(t != 0) t /= 10, ++d;  
          
        int left = pow(10, d - 1);  
        int right = 1;  
        while( left >= right)  
        {  
            if (x / left % 10 != x / right % 10)  
                return false;  
              
            left /= 10;  
            right *= 10;  
        }  
        return true;  
"""