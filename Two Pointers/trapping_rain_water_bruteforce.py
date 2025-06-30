from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        # we take min of 2 block that is the bottleneck, that gives how much water we can trap.
        #so for between the blocks we do min (L, R) - h[i]
        # way 1 - brutforce
        if not height:
            return 0
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i + 1, n):
                rightMax = max(rightMax, height[j])
                
            res += min(leftMax, rightMax) - height[i]
        return res
