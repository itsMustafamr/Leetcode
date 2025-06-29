from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # way 2 - dont use this - not allowed division method
        total_product = 1
        zero_count = nums.count(0)

        # Case 1: More than 1 zero → all products will be 0
        if zero_count > 1:
            return [0] * len(nums)

        # Case 2: Exactly one zero → only one index will be non-zero
        if zero_count == 1:
            result = [0] * len(nums)
            zero_index = nums.index(0)
            for i, val in enumerate(nums):
                if i != zero_index:
                    total_product *= val
            result[zero_index] = total_product
            return result