# @Author: Luoxin Fan
# @Date: 2024-06-14 : 13:41
class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        moves = 0;

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                prev = nums[i]
                nums[i] = nums[i - 1] + 1;
                moves += nums[i] - prev

        return moves


if __name__ == '__main__':
    print(Solution.minIncrementForUnique(Solution, [3, 2, 1, 2, 1, 7]))
