#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Given a string, find the length of the longest substring without repeating characters.

# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        walker = runner = 0
        maxlen = 0
        length = len(s)
        dic = {}

        while runner != length:
            if s[runner] in dic and walker <= dic[s[runner]]:
                walker = dic[s[runner]] + 1
            else:
                maxlen = max(maxlen, runner - walker + 1)
            dic[s[runner]] = runner
            runner += 1

        return maxlen


if __name__ == '__main__':
    solution = Solution()
    print solution.lengthOfLongestSubstring('pwwkew')
