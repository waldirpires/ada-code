# Backtracking / brute force


'''
0000
0001
0010
0011
0100
...
1111
'''

def binaryLoops():
  for i in range(2):
    for j in range(2):
      for k in range(2):
        for l in range(2):
            print(i,j,k,l)

#binaryLoops()

def binaryRecursion(n, partial):
  if len(partial)==n:
    print(partial)
  else:
    for c in "01":
      binaryRecursion(n, partial+c)

#binaryRecursion(4, "")
#binaryRecursion(8, "")

#[1, 2, 3]

#[1, 2, 3]
#[1, 2]
#[1, 3]
#[1]
#[2, 3]
#[2]
#[3]
#[]

def subsets(arr, index, partial):
  if index>=len(arr):
    return [partial]
  else:
    #in and out
    inSolutions = subsets(arr, index+1, partial+[arr[index]])
    outSolutions = subsets(arr, index+1, partial)
    return outSolutions + inSolutions

#solutions = subsets([1, 2, 3], 0, [])
#for solution in solutions:
#  print(solution)

#https://leetcode.com/problems/subsets/

def permutationWithRepetition(n, arr):
  if len(arr)==n:
    print(*arr)
  else:
    for i in range(1, n+1):
      arr.append(i)
      permutationWithRepetition(n, arr)
      arr.pop(-1)

#permutationWithRepetition(4, [])

def permutation(n, arr):
  if len(arr)==n:
    print(*arr)
  else:
    for i in range(1, n+1):
      if i not in arr:
        arr.append(i)
        permutation(n, arr)
        arr.pop(-1)

#permutation(4, [])
#permutation(8, [])

#https://leetcode.com/problems/permutations/

def combinations(n, k, partial):
  if len(partial)==k:
    solutions = [partial]
  elif len(partial)==0:
    solutions = []
    for i in range(1, n+1):
      solutions += combinations(n, k, [i])
  else:
    lastFromPartial = partial[-1]
    solutions = []
    for i in range(lastFromPartial+1, n+1):
      solutions += combinations(n, k, partial+[i])
  return solutions

#solutions = combinations(4, 2, [])
#solutions = combinations(5, 3, [])
#for solution in solutions:
#  print(solution)


# combinations in an array with repetitions
def powerSets(arr):
  arr.sort()
  solutions = []
  def combinationsNotUnique(arr, index, partial):
    if index>=len(arr):
      if len(solutions)==0 or solutions[-1]!=partial:
        solutions.append(partial)
    else:
      #in and out
      combinationsNotUnique(arr, index+1, partial+[arr[index]])
      combinationsNotUnique(arr, index+1, partial)
  combinationsNotUnique(arr, 0, [])
  return solutions


#https://leetcode.com/problems/combinations/

solutions = powerSets( [1, 2, 2] )
for solution in solutions:
  print(solution)


# Problemas do LeetCode

#https://leetcode.com/problems/subsets/
class Subsets:
  def subsets(self, nums):
      solutions = []
      partial = []
      def backtracking(index):
          if index>=len(nums):
              solutions.append(partial.copy())
          else:
              backtracking(index+1)

              partial.append(nums[index])
              backtracking(index+1)
              partial.pop(-1)
          return solutions
      backtracking(0)
      return solutions

#https://leetcode.com/problems/permutations/
class Permutations:
# Solution with in : linear search, 51ms, beats 6.46%

#    def permute(self, nums: List[int]) -> List[List[int]]:
#        solutions = []
#        partial = []
#
#        def backtracking(index: int):
#            if index>=len(nums):
#                solutions.append(partial.copy())
#            else:
#                for num in nums:
#                    if num not in partial:
#                        partial.append(num)
#                        backtracking(index+1)
#                        partial.pop(-1)
#
#        backtracking(0)
#        return solutions

    def permute(self, nums) :
        solutions = []
        partialSet = set()

        def backtracking(index: int, partial):
            if index>=len(nums):
                solutions.append(partial)
            else:
                for num in nums:
                    if num not in partialSet:
                        partialSet.add(num)
                        backtracking(index+1, partial + [num])
                        partialSet.remove(num)

        backtracking(0, [])
        return solutions


class Combinations:

  def bruteForce(self, n, k, vet, output):
      if len(vet)==k:
          output.append(vet[:])
      else:
          for i in range(1, n+1):
              if len(vet)==0 or i>vet[-1]:
                  vet.append(i)
                  self.bruteForce(n, k, vet, output)
                  vet.pop(-1)


  def combine(self, n: int, k: int):
      output = []
      self.bruteForce(n, k, [], output)
      return output
