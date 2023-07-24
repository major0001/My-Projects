from typing import List

class Solution:
    def findMedianSortedArray(self, nums1: List[int], nums2: List[int]) -> int:
        # the list to which we combine the two lists
        merged = []

        # combine two the lists into one
        i, j = 0, 0

        while i < len(nums1)  and len(nums2):
            if nums1[i] <= nums2[j]:
                
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1


        # merge the remaining elements in both lists
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1


        # now let's find the median
        n = len(merged)
        
        # when n is even

        if n % 2 == 0:
            median = merged[n // 2 - 1 ] + merged[n // 2] / 2

        else:
            median = merged[n // 2]



        return median


# example
sol = Solution()

nums1 = [1, 2, 4, 5, 6, 7, 8]
nums2 = [3, 9]

nums3 = [30, 34, 34, 35, 36, 38]
nums4 = [39]
print(sol.findMedianSortedArray(nums1, nums2))
print(sol.findMedianSortedArray(nums3, nums4))

print()
nums5 = [1,2,4,5,6,7]
nums6 = [3,8]
print(sol.findMedianSortedArray(nums5, nums6))

