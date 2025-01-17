class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums = set(nums)
        max_len = 0
        for i in nums: # para cada numero na lista
            # se seu antecessor existir, devemos começar por ele e não o corrente (quando o laço chegar)
            if i-1 not in nums: # se seu antecessor não existir na lista
                curr_ele = i
                maxlen = 1
                while curr_ele+1 in nums: # se o próximo valor estiver no vetor
                    curr_ele += 1 # incrementa o corrente
                    maxlen += 1 # atualiza o contador de tamanho
                max_len = max(max_len ,maxlen) # atualiza o maxLen encontrado até o momento
        return max_len

s = Solution()
r = s.longestConsecutive([100,4,200,1,3,2])
print(r)

# https://leetcode.com/problems/longest-consecutive-sequence/description/