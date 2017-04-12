#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#       Given nums = [2, 7, 11, 15], target = 9,
#
#       Because nums[0] + nums[1] = 2 + 7 = 9,
#       return [0, 1].

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 时间复杂度O(n²), 空间复杂度O(1)
    # rst = []
    # for i, val in enumerate(nums):
    #     for j, num in enumerate(nums):
    #         if i != j:
    #             if val + num == target:
    #                 rst = [i, j]
    #                 break
    # return rst

    # 时间复杂度O(n)，空间复杂度O(n)
    dic = {}
    for idx, val in enumerate(nums):
        complement = target - val
        if dic.has_key(complement):
            return [dic.get(complement), idx]
        dic.update({val: idx})


result = two_sum([1, 2, 3, 4, 5, 6], 9)
print result

