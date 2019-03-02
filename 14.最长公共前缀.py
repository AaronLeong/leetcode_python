#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (32.00%)
# Total Accepted:    53.1K
# Total Submissions: 165.7K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 示例 1:
# 
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 
# 
# 示例 2:
# 
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 
# 
# 说明:
# 
# 所有输入只包含小写字母 a-z 。
# 
#
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    # def longestCommonPrefix(self, strs):
        if len(strs)>0:
          
            # 记录公共前缀
            cur_p = ''
            # 默认第一个字符串作为基础比较
            s = strs[0]
            # 记录字符串最小长度
            MIN_S = len(s)
            # 循环索引
            i = 0
            while i < MIN_S:
                # 第 i 个字符串
                si = s[i]
                # 循环比较其他字符串
                for j in strs[1:]:
                    # 更新最小字符长度
                    # 最长的公共前缀就是最短字符的长度了，再比较就没有意义了
                    if len(j)<MIN_S:
                        MIN_S = len(j)
                    # 检测字符串开头
                    if not j.startswith(cur_p+si):
                        # 如果不是这个字符串不是 cur_p+si 开头，最大的公共前缀就是cur_p
                        return cur_p
                i+=1
                # 记录公共前缀
                cur_p = cur_p+si
        else:
            return ''
        return cur_p


# # ["flower","flow","flight"]
# print(Solution().longestCommonPrefix(["flower","flow","flight"]))

        

