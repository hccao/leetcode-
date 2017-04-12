#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next_node = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        multiplier1 = 1
        sum1 = 0
        while l1 is not None:
            sum1 += l1.val * multiplier1
            l1 = l1.next_node
            multiplier1 *= 10

        multiplier2 = 1
        sum2 = 0
        while l2 is not None:
            sum2 += l2.val * multiplier2
            l2 = l2.next_node
            multiplier2 *= 10

        sum_rst = sum1 + sum2

        sum_lst = list(str(sum_rst))
        sum_lst = sum_lst[::-1]
        rst_node1 = ListNode(int(sum_lst[0]))
        rst_node_last = rst_node1
        for idx, item in enumerate(sum_lst):
            if idx != 0:
                node = ListNode(int(sum_lst[idx]))
                rst_node_last.next_node = node
                rst_node_last = node

        return rst_node1


if __name__ == '__main__':
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node1.next_node = node2
    node2.next_node = node3

    node4 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    node4.next_node = node5
    node5.next_node = node6

    solution = Solution()
    rst_node = solution.addTwoNumbers(node1, node4)
    # while rst_node is not None:
    #     print rst_node.val
    #     rst_node = rst_node.next_node
