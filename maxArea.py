from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Initialize two pointers at the beginning and end of the height lis
        left = 0
        right =  len(height) - 1

        max_area = 0

        while left < right:
            # calculate the current area
            area = min(height[left], height[right]) * (right - left)

            # Update the maximum area if necessary
            max_area = max(max_area, area)

            # move the pointer with the smallest height
            if height[left] < height[right]:
                left += 1

            else:
                right -= 1


        return max_area

# examples
sol  = Solution()
h = [1,38,6,2,5,4,8,3,7]
ans = sol.maxArea(h)
print(ans)
