#cheating basically. counter is a datastructure in python which is a hashmap which counts things automatically for you 

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

solution = Solution()

s = input("Enter the first string: ")
t = input("Enter the second string: ")


result = solution.isAnagram(s, t)
print(f"Are '{s}' and '{t}' anagrams? {result}")