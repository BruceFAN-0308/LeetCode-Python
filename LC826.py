class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = [[0, 0] for _ in range(len(difficulty))]
        for i in range(len(difficulty)):
            jobs[i][0] = difficulty[i]
            jobs[i][1] = profit[i]

        jobs.sort(key=lambda o: o[0])
        worker.sort()
        ans = 0
        j = 0
        max_profit = 0
        for w in worker:
            while j < len(difficulty) and w >= jobs[j][0]:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            ans += max_profit
        return ans


if __name__ == '__main__':
    print(Solution.maxProfitAssignment(Solution,
                                       [2, 17, 19, 20, 24, 29, 33, 43, 50, 51, 57, 67, 70, 72, 73, 75, 80, 82, 87, 90],
                                       [6, 7, 10, 17, 18, 29, 30, 31, 34, 39, 40, 42, 48, 54, 57, 78, 78, 78, 83, 88],
                                       [12, 9, 11, 41, 11, 87, 48, 6, 48, 93, 76, 73, 7, 50, 55, 97, 47, 33, 46, 10]))
