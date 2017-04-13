# Reverse digits of an integer.

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# Note:
# The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        num = abs(x)
        num_list = list(str(num))

        rst = 0
        step = 1
        for item in num_list:
            rst += int(item) * step
            step *= 10

        if num > 0x7FFFFFFF:
            return 0
        elif x < 0:
            return -rst
        else:
            return rst


if __name__ == '__main__':
    solution = Solution()
    print solution.reverse(123)
    print solution.reverse(-123)
