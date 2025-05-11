from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element using Counter
        count = Counter(nums)
        
        # Step 2: Use the most_common method from Counter to get the top k frequent elements
        # most_common returns a list of tuples (element, frequency), so we need to extract only the elements
        most_frequent = [item for item, freq in count.most_common(k)]
        
        # Step 3: Return the k most frequent elements
        return most_frequent

# Input and Output handling
sol = Solution()
input_value = input("Enter a list of numbers with spaces: ")
k = int(input("Enter the value of k: "))

num = list(map(int, input_value.split()))

result = sol.topKFrequent(num, k)
print("The top", k, "most frequent elements are:", result)
