from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        frequency_dict = {}
        for num in nums:
            if num in frequency_dict:
                frequency_dict[num] += 1
            else:
                frequency_dict[num] = 1
        
        # Step 2: Use a min-heap to keep track of the top k frequent elements
        heap = []
        
        # Go through each element in the frequency dictionary
        for num, freq in frequency_dict.items():
            # Push the tuple (frequency, num) into the heap
            heapq.heappush(heap, (freq, num))
            
            # If the size of the heap exceeds k, pop the smallest element (min-heap)
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Extract the elements from the heap
        top_k_frequent = [num for freq, num in heap]
        
        return top_k_frequent

# Input and Output handling
sol = Solution()
input_value = input("Enter a list of numbers with spaces: ")
k = int(input("Enter the value of k: "))

num = list(map(int, input_value.split()))

result = sol.topKFrequent(num, k)
print("The top", k, "most frequent elements are:", result)
