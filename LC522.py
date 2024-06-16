class Solution:
    def findLUSlength(self, strs):
        def subseq(w1, w2):
            if len(w1) > len(w2):
                return False
            i = 0
            for c in w2:
                if i < len(w1) and w1[i] == c:
                    i += 1
            return i == len(w1)

        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            if all(not subseq(word1, word2)
                   for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1


if __name__ == '__main__':
    print(Solution.findLUSlength(Solution, ["aaa", "aaa", "aa"]))
