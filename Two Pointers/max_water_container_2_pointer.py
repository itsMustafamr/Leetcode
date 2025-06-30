from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #way 2 - 2 pointer
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            # elif heights[l] > heights[r]:
            #     r -= 1
            else:
                r -= 1

        return res