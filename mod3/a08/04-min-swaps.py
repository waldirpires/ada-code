import sys

class Solution:
    def dp(self, nums1, nums2, prev1, prev2, i, swapped, lookup):
        # se chegarmos no final do vetor
        if i == len(nums1):
            return 0

        key = (i, swapped)
        if key not in lookup:
            minSwaps = sys.maxsize
            # Swap
            if nums2[i] > prev1 and nums1[i] > prev2:
                minSwaps = 1 + self.dp(nums1, nums2, nums2[i], nums1[i], i+1, 1, lookup)
            # Dont swap
            if nums2[i] > prev2 and nums1[i] > prev1:
                minSwaps = min(minSwaps, self.dp(nums1, nums2, nums1[i], nums2[i], i+1, 0, lookup))
            # step 2: salvar o valor no dicionario
            lookup[key] = minSwaps

        # step 3: usar dicionário
        return lookup[key]

    def minSwap(self, nums1, nums2):
        # step 1: criação do dicionario
        lookup = {}
        return self.dp(nums1, nums2, -1, -1, 0, 0, lookup)

s = Solution()
nums1 = [1,3,5,4]
nums2 = [1,2,3,7]
r = s.minSwap(nums1, nums2)
print(r)