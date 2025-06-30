from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #way 2 - two pointer - best 
        l = 0
        r = len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r = r - 1
            if curSum < target:
                l = l + 1
            if curSum == target: # or else:
                return [l + 1, r + 1]
        return []
        


