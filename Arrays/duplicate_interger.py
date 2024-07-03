#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# Create an instance of the Solution class
solution = Solution()

# Take input from the user
input_str = input("Enter a list of numbers separated by spaces: ")

# Convert the input string to a list of integers
nums = list(map(int, input_str.split()))

# Check for duplicates and print the result
result = solution.hasDuplicate(nums)
print(f"Does the array {nums} have duplicates? {result}")
