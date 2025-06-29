from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # way 2 - brut force
        longest = 0
        for num in nums:
            length = 1
            current = num
            while current + 1 in nums:
                current += 1
                length += 1
            longest = max(longest, length)
        return longest
