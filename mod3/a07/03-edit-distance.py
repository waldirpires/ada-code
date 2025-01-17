class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def helper(w1, w2):
            if w2 == len(word2):
                return len(word1) - w1
            if w1 == len(word1):
                return len(word2) - w2
            if word1[w1] == word2[w2]:
                return helper(w1 + 1, w2 + 1)

            return 1 + min(helper(w1 + 1, w2), helper(w1 + 1, w2 + 1), helper(w1, w2 + 1))

        return helper(0, 0)

