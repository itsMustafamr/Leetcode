import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #way 2 - binary search - O(log m * n) - O(n log m)
        l, r = 1, max(piles)
        res = r # only cuz we are looking for minimum so we didn't initialize to 0 
        # r which is the max of the pile

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            
            else:
                l = k + 1
            
        return res

