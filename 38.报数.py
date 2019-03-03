#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
# https://leetcode-cn.com/problems/count-and-say/description/
#
# algorithms
# Easy (48.11%)
# Total Accepted:    21.4K
# Total Submissions: 44.6K
# Testcase Example:  '1'
#
# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 
# 给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。
# 
# 注意：整数顺序将表示为一个字符串。
# 
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "1"
# 
# 
# 示例 2:
# 
# 输入: 4
# 输出: "1211"
# 
# 
#
class Solution:
    def countAndSay(self, n: int) -> str:
       
        s = '1'
        res = ''
        c = 0
        c_s = None
        flag = False
        
        while n-1:

            res = s
            s = ''

            for i,si in enumerate(res):

                if not c_s:
                    c_s = si
                    c += 1
                else:
                    c += 1
                
            
                if i+1 < len(res):
                    if si != res[i+1]:
                        # print('False 1')
                        flag = True
                elif i+1 == len(res):
                    # print('False 2')
                    flag = True

                # print('c ,c_s', c ,c_s, flag)
                if flag:
                    if s == '':

                        s = str(c)+str(c_s)
                    else:
                        s = s + str(c)+str(c_s)
                    c_s = None
                    c = 0
                    flag = False
                    
            n -= 1
            # res 
                
        return s
                


print('res',Solution().countAndSay(5))
        

