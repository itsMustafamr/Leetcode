from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we basically compute prefix of the number left to i and
        # we take the postfix of the number right to i 
        # multiply prefix and postfix values...
        # to save memory we multiply prefix and postfix while computing on iteration tgr

        # way 1 - optimal
        res = [1] * (len(nums)) # result output array

        prefix = 1 
        for i in range(len(nums)): # every position in our output array
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
        # way 2 - dont use this - not allowed division method
        # total_product = 1
        # zero_count = nums.count(0)

        # # Case 1: More than 1 zero → all products will be 0
        # if zero_count > 1:
        #     return [0] * len(nums)

        # # Case 2: Exactly one zero → only one index will be non-zero
        # if zero_count == 1:
        #     result = [0] * len(nums)
        #     zero_index = nums.index(0)
        #     for i, val in enumerate(nums):
        #         if i != zero_index:
        #             total_product *= val
        #     result[zero_index] = total_product
        #     return result

        # # Case 3: No zeros → use division
        # for num in nums:
        #     total_product *= num

        # return [total_product // num for num in nums]
        # way 3
        # n = len(nums)
        # prefix = [1] * n
        # suffix = [1] * n
        # res = [0] * n

        # for i in range(1, n):
        #     prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # for i in range(n - 2, -1, -1):
        #     suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # for i in range(n):
        #     res[i] = prefix[i] * suffix[i]
        
        # return res
        # way 4 - easier numbering
        # res = [1] * len(nums)

        # left = 1
        # for i in range(len(nums)):
        #     res[i] = left
        #     left *= nums[i]
        
        # right = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     res[i] *= right
        #     right *= nums[i]
        
        # return res
