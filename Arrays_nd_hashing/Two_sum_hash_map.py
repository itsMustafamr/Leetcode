from typing import List
# run time of O(n)
# here the hasmap is used as a value and index as a key (value:index) - usually different
# target - val 
# in hasmap it will be stored as val : key but value will be after target - val so when we find a value that can be added to target
# then we find its true
# so we can do it in O(n)
# space - O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # ie maping of val : index - ie every previous element will be stored here in the hashmap

        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return()
    
    
