# here we do sorting and then compare in pair so only need to iterate once after sorting
# time - o(nlog(n))
# space - o(1) - no extra space
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort() # sort it as 1, 2,3,3 ,4 then comparies in pair or write the whole code
        # for (i in range(len(nums)):
        #for (j in range(0, len(nums))-i-1)):
        # if (nums[j] > nums[j+1]):
        #nums[j], nums[j+1] = nums[j+1], nums[j] or temp = nums[j]
        #nums[j] = nums[j+1]
        #nums[j+1] = temp
        for i in range(len(nums) - 1): #or len(nums) = n and for i in range(n-1):
            if nums[i] == nums[i + 1]:  
                return True
        return False

sol = Solution()
input_value = input("Enter a list of numbers with spaces")

num = list(input_value.split())

result = sol.hasDuplicate(num)
print("does numbers have duplicate", result)
print(num)
