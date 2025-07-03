import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #way 1 - brutforce - O(max(pile) * pile) - O(m * n)
        speed = 1
        while True:
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / speed)
            
            if totalTime <= h:
                return speed
            speed += 1
        return speed
