from typing import List


class Solution(object):
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1;

        min_value = min(bloomDay)
        max_value = max(bloomDay)
        while min_value < max_value:
            mid = (max_value - min_value) // 2 + min_value
            if can_make(bloomDay, m, k, mid):
                max_value = mid
            else:
                min_value = mid + 1

        return min_value


def can_make(bloom_day, m, k, days) -> bool:
    bouquets = 0
    flower = 0
    for i in bloom_day:
        if days >= i:
            flower += 1
            if flower == k:
                bouquets += 1
                flower = 0
        else:
            flower = 0;
    return bouquets >= m


if __name__ == '__main__':
    print(Solution.minDays(Solution, [62, 75, 98, 63, 47, 65, 51, 87, 22, 27, 73, 92, 76, 44, 13, 90, 100, 85], 2, 7))
