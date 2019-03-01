#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#
# https://leetcode-cn.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (56.82%)
# Total Accepted:    41K
# Total Submissions: 72.2K
# Testcase Example:  '"III"'
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
# 
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
# 
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
# 
# 
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 
# 
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
# 
# 示例 1:
# 
# 输入: "III"
# 输出: 3
# 
# 示例 2:
# 
# 输入: "IV"
# 输出: 4
# 
# 示例 3:
# 
# 输入: "IX"
# 输出: 9
# 
# 示例 4:
# 
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
# 
# 
# 示例 5:
# 
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
# 
#
class Solution:
    def romanToInt(self, s: str) -> int:
       
        Smap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        Os = ['I','V','X','L','C','D','M']
        sl = list(s)
        cur_index = 0

        num = 0 
        i = 0
        l = len(sl)
        # 循环读取每一个字符
        while i < l:
            s = sl[i]
            # 判断还有没有下一个字符
            if i+1 < l:
                
                # 获取当前字符与下一个字符的大小
                # 用于检测这两个字符的计算方式
                # 如果后一个数比前一个大，用后一个减前一个数
                # 否则前后两个字符是相加方式
                si = Os.index(s)
                sli = Os.index(sl[i+1])
                # 如果后一个数比前一个大，用后一个减前一个数
                if si < sli:
                    num = num + Smap[sl[i+1]] - Smap[s]
                   
                    # 因为当前字符与后一个字符一起表示一个数，所以后一个字符直接跳过
                    i = i+2
                else:
                    # 前后两个字符是相加方式 
                    # 后一个字符放到下一次计算中
                    # 这里不能 直接 Smap[sl[i+1]] + Smap[s]的原因是 sl[i+1] 与 sl[i+2] 可能表示一个数
                    num = num + Smap[s]
                    i = i+1
                # print(num)
            else:
                i = i+1
                num = num + Smap[s]

                
            
        return num

print(Solution().romanToInt('MCMXCIV'))


