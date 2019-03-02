#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.44%)
# Total Accepted:    47.9K
# Total Submissions: 131.5K
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 注意空字符串可被认为是有效字符串。
# 
# 示例 1:
# 
# 输入: "()"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: "()[]{}"
# 输出: true
# 
# 
# 示例 3:
# 
# 输入: "(]"
# 输出: false
# 
# 
# 示例 4:
# 
# 输入: "([)]"
# 输出: false
# 
# 
# 示例 5:
# 
# 输入: "{[]}"
# 输出: true
# 
#
class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


#  我傻逼了  。。。。可能是昨晚失眠只睡了4个小时吧。。。
# class Solution:
#     def isValid(self, s: str) -> bool:
#         s = list(s)
#         if len(s)==0:
#             return True
#         elif len(s)%2!=0:
#             return False
#         else:
#             max_loop = int(len(s)/2)
#             i = 0
#             s_map = {
#                 '}':'{',
#                 '{':'}',
#                 ']':'[',
#                 '[':']',
#                 ')':'(',
#                 '(':')'
#             }
#             while max_loop:
#                 print('max_loop', max_loop)
#                 print(s)
#                 if s[i]==s_map[s[i+1]]:
#                     print(1)
#                     # print(s_map[s[i+1]])
#                     max_loop-=1
#                     del s[1]
#                     del s[0]
                    
#                     # continue
                    
                    
#                 elif s[i]==s_map[s[-1-i]]:
#                     print(2)
#                     del s[0]
#                     del s[-1]
#                     max_loop-=1
                   
#                 else:
#                     tag = False
#                     if max_loop%2==0: 
#                         sl = max_loop+1
#                     else:
#                         sl = max_loop
#                     for x,j in enumerate(s[1:sl]):
#                         print(s[i],x,j)
#                         if s_map[j] == s[i] and (x)%2==0:
#                             print(3)

#                             del s[x+1]
#                             del s[0]
                            
#                             # print(x)
#                             tag = True
                           
#                             continue
#                     if not tag:
#                         return False
#                 max_loop = int(len(s)/2)
#             return True
# ()[]{}
# ([)]
# (([]){})
# [([]])
# print(Solution().isValid('()[]{}'),True)
# print(Solution().isValid('([)]'),False)
# print(Solution().isValid('(([]){})'),True)
# print(Solution().isValid('[([]])'),False)


        

