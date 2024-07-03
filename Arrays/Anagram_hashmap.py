#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)  != len(t):
            return False
        
        countS, countT = {},{} # declaring hashmaps
        for i in range(len(s)):
            #countS[s[i]] = 1 + countS[s[i]] no because in python this will trow an error, key doesnot exist  # counting each carecter in stringS
            countS[s[i]] = 1 + countS.get(s[i], 0) # get wit hashmap so to get this key ie s[i] and second parameter is just a default value that will return 0 if key does not exist
            countS[t[i]] = 1 + countS.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        

        return True

solution = Solution()

s = input("Enter the first string: ")
t = input("Enter the second string: ")


result = solution.isAnagram(s, t)
print(f"Are '{s}' and '{t}' anagrams? {result}")