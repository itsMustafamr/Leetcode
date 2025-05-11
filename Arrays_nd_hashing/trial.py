from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}#mapping charecter count to list of anagrams

        for s in strs:
            count = [0] * 26 #we will have 26 0s ie from a....z

            for c in s: 
                count[ord(c) - ord("a")] += 1 #this counts how many of each charecter we have
                # #here ord() is basically the asicii value so it will be like if 
                # 1st element is "a" then a = 80 -> 0, 80-80 then b = 81 -> 1, 81-80


        