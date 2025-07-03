from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2
            if nums[mid] < target:
                L = L + 1
            elif nums[mid] > target:
                R = R - 1
            else:
                return mid
    
        return -1
        