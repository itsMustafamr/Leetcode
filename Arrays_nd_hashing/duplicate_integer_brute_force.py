#runtime - o(n^2) - have to compare it to rest of the numbers in the array and to the size of the array
#space - o(1) - no extra memory needed

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
            
        return False

# sol = Solution()
# in_value = input("enter values in list")
# num = list(in_value.split())
# result = sol.hasDuplicate(num)
# print("result of duplicate numbers", result)

# a = Solution()
# val = input("values of list")
# # num = list(split(val))
# num = list(val.split())
# result = a.hasDuplicate(num)
# print("duplicate list",result)
# or


val = input("values of list")
num = list(val.split())
result = Solution().hasDuplicate(num)
print("duplicate list",result)