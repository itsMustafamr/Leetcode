from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        #number of empty arrays is equal to the length of nums + 1

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
        # here we go from the end of the array to the beginning the -1 is to start from the end     
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res