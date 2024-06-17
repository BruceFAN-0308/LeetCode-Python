import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = math.floor(math.sqrt(c))
        while left <= right:
            sum = left * left + right * right
            if sum == c:
                return True
            elif sum < c:
                left += 1
            else:
                right -= 1
        return False


if __name__ == '__main__':
    print(Solution.judgeSquareSum(Solution, 2147483600))
