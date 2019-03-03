#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (52.58%)
# Total Accepted:    45.2K
# Total Submissions: 86K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        if l1==None and l2==None:
            result=None
           
        elif l1==None:
            result=l2
    
        elif l2==None:
            result=l1
            
        else:
            # 
            n = 0
            #  node
            #  初始化 保存节点
            while l1 and l2:
               
                if l1.val<l2.val:
                    
                    if n == 0:
                        result = ListNode(l1.val)
                        # result 是 n 的容器
                        # 第一个节点 后面修改的n是递归的节点 不会改变result
                        n = result
                    else:
                       
                        n.next = ListNode(l1.val)
                        n = n.next
                        
                    l1 = l1.next
                    # 如果l1已经没有值了 直接把l2 放再后面
                    if not l1:
                        n.next = l2
                else:
                    if n == 0:
                        result = ListNode(l2.val)
                        n = result
                    else:
                        n.next = ListNode(l2.val)
                        n = n.next
                    l2 = l2.next
                    
                    if not l2:
                        n.next = l1
        
        return result 
                    
            
            
            
            
        
        

