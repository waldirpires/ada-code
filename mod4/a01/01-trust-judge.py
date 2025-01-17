class Solution(object):
    # O(n) time
    # O(n) space
    def findJudge(self, n, trust):
        if len(trust)==0 and n==1:
            return 1
        # vetor para armazenar a pontuação de confiança entre as pessoas
        c=[0]*(n+1)
        # contabilizar as confianças entre pessoas
        for i in trust:
            c[i[0]]-=1
            c[i[1]]+=1

        print(c)
        # se encontrarmos alguém que não confia em ninguém
        for i in range(len(c)):
            if c[i]==n-1:
                return i
        return -1

s = Solution()
n = 2
trust = [[1,2]]
r = s.findJudge(n, trust)
print(r)