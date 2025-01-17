class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        #memo of size len(arr) with -1's
        # step 1: usar um vetor para memorização
        memo = [-1]*len(arr)
        #lis in last position = 1
        memo[len(arr)-1] = 1
        #from end to 0
        for i in range(len(arr)-2, -1, -1):
            maxSequence = 0
            # buscando por valores maiores que o corrente
            for j in range(i+1, len(arr)):
                # se o valor for maior
                if arr[j]>arr[i]:
                    # buscar a seq. máxima dentro de memo
                    # step 2: usar o memo para ajudar a resolver o problema
                    maxSequence = max(maxSequence, memo[j])
            # step 3: salvar a solução parcial em memo
            memo[i] = 1+maxSequence
        #return max value from memo
        return max(memo)

s = Solution()
nums = [10,9,2,5,3,7,101,18]
r = s.lengthOfLIS(nums)
print(r)
