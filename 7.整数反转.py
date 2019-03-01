#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (31.66%)
# Total Accepted:    84.8K
# Total Submissions: 267.7K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        # 检测符号
        z = 1
        if x<0:
            z = -1
        
        INT_MAX = 2**31-1
        INT_MIN = -2**31

        t = str(abs(x))
        l=list(t)
        l.reverse()
       
        if len(l)>9:
        # 如果是10位数才需要检测 是否溢出
            y = int("".join(l[:-1]))
            if y > INT_MAX/10:
                # 如果最高位都比最大值大，最后一位无论是什么都会溢出
                return 0
            elif(int(l[-1])>7):
                # 前面9位数不溢出 才检测最后一位数
                return 0
            return (y*10+int(l[-1]))*z
        else:
            # 如果小于9位数 直接反转 + 符号
            return int("".join(l))*z

