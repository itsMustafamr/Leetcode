from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
            
        return False

sol = Solution()
in_value = input("enter values in list")
num = list(in_value.split())
result = sol.hasDuplicate(num)
print("result of duplicate numbers", result)
