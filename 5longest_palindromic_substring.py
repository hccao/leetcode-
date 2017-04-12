class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        max_s = ''
        for idx, val in enumerate(s):
            for i in [1, 2]:  # 奇偶对称判断
                step = 0
                while idx - step >= 0 and idx + (i - 1) + step < len(s):
                    last_s = s[idx - step]
                    next_s = s[idx + (i - 1) + step]
                    if last_s == next_s:
                        max_len = step * 2 + i
                        if max_len > len(max_s):
                            max_s = s[(idx - step):(idx + step + i)]
                        step += 1
                    else:
                        break
        return max_s

# https://discuss.leetcode.com/topic/7144/python-o-n-2-method-with-some-optimization-88ms
