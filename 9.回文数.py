#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (56.07%)
# Total Accepted:    73.4K
# Total Submissions: 130.9K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
# 
# 示例 1:
# 
# 输入: 121
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 
# 
# 示例 3:
# 
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 
# 
# 进阶:
# 
# 你能不将整数转为字符串来解决这个问题吗？
# 
#
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x == 0:
            return True

        if x<0 or x%10==0:
            return False

        else:
            l = len(str(x))
            # if l%2==0:
            #     return False
            # print(l, int(l/2)+1)
            # 把整数对半取
            for i in range(1,int(l/2)+1):
                # print(i, int(x/(10**(l-i))))

                # int(x/(10**(l-i))) 取前i位数
                # %10 取第i位数 789 中的9
                k = int(x/(10**(l-i)))%10

                #  x%(10**i)取后i位数
                # 取后i位数/(10**(i-1)) 取后i位数的第一位 789 中的7
                y = int((x%(10**i))/(10**(i-1)))
                # print(k,y)
                # 看相不相等
                if k != y:
                    return False
        
            return True

print(Solution().isPalindrome(123))
                



