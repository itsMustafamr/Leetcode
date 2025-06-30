from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #way 1- brut force and pointers
        res = 0 # result 
        for l in range(len(heights) - 1):
            for r in range(l + 1, len(heights)):
                area = (r - l) * min(heights[l], heights[r]) # a = width * height
                res = max(res, area) # we basically want the maximum area
        return res