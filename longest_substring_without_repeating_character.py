#!/usr/bin/env python
# -*- coding: utf-8 -*-


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
