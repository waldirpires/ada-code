class Solution:
    def readBinaryWatch(self, turnedOn):
        choices = [('h', 1), ('h', 2), ('h', 4), ('h', 8), ('m', 1), ('m', 2), ('m', 4), ('m', 8), ('m', 16), ('m', 32)]

        res = []
        def dfs(hour, minute, left, idx):
            if hour > 11 or minute > 59: # caso base
                return
            if left == 0: # caso base
                res.append(f'{hour}:{minute:02}')
                return
            for i in range(idx, len(choices)):
                time_type, val = choices[i]
                if time_type == 'h':
                    dfs(hour + val, minute, left - 1, i + 1) # passo recursivo para hora
                else:
                    dfs(hour, minute + val, left - 1, i + 1) # passo recursivo para minuto

        dfs(0, 0, turnedOn, 0)
        return res

solution = Solution()
solutions = solution.readBinaryWatch(8)
for solution in solutions:
  print(solution)