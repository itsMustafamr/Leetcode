from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_elements = sorted(count.items(), key = lambda x:x[1], reverse=True)

        top_k = [element for element, frequency in sorted_elements[:k]]        

        return top_k

# Example usage
solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(solution.topKFrequent(nums, k))  # Output: [1, 2]     