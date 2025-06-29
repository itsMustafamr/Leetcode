from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # way 1 - sorting
        nums.sort()
        longest = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # skip duplicates
            elif nums[i] == nums[i - 1] + 1:
                curr += 1
                longest = max(longest, curr)
            else:
                curr = 1

        return longest


