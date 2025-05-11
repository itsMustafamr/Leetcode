from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        # Step 2: Sort the elements by frequency
        # Convert the dictionary items into a list of tuples and sort by the frequency
        sorted_elements = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Extract the top k elements
        top_k_frequent = [item for item, freq in sorted_elements[:k]]
        
        # Step 4: Return the result
        return top_k_frequent

# Input and Output handling
sol = Solution()
input_value = input("Enter a list of numbers with spaces: ")
k = int(input("Enter the value of k: "))

num = list(map(int, input_value.split()))

result = sol.topKFrequent(num, k)
print("The top", k, "most frequent elements are:", result)
