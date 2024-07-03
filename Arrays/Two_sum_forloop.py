from typing import List
#runtime of n^2

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return i, j

        return()

solution = Solution()

nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
target = int(input("Enter the target number: "))

result = solution.twoSum(nums, target)
print(f"The indices are: {result}")

Print("hurray")