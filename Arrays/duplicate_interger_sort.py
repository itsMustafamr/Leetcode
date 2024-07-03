from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # sort it as 1, 2,3,3 ,4 then comparies in pair
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:  
                return True
        return False

sol = Solution()
input_value = input("Enter a list of numbers with spaces")

num = list(input_value.split())

result = sol.hasDuplicate(num)
print("does numbers have duplicate", result)
