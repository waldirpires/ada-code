class Solution:
    def kthDistinct(self, arr, k):
        if k == 0 or not arr: # dealing with invalid params
            return ""

        map = {} # create empty map/dictionary

        for s in arr: # populate with frequencies
            map[s] = map.get(s, 0) + 1

        cnt = 0 # counter

        for s in arr: # walk through the map
            if map[s] == 1: # if there is only one occurence
                cnt += 1 # increment counter

            if cnt == k: # once counter reaches k, return result
                return s

        return "" # return empty if none

arr = ["d","b","c","b","c","a"]
k = 2
s = Solution()
r = s.kthDistinct(arr, k)
print(r)