#from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            # Sort the string and use it as a key
            sorted_str = ''.join(sorted(s))
            anagrams[sorted_str].append(s)
        
        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())

def main():
    # Input function to read the list of strings
    strs = input("Enter the list of strings (comma-separated): ").split(',')
    
    # Trim any leading/trailing spaces from each string
    strs = [s.strip() for s in strs]

    # Create an instance of the Solution class
    solution = Solution()

    # Group the anagrams
    result = solution.groupAnagrams(strs)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()





#1
# #m.nlogn
# from collections import defaultdict

# def group_anagrams(strs):
#     anagrams = defaultdict(list)
    
#     for s in strs:
#         # Sort the string and use it as a key
#         sorted_str = ''.join(sorted(s))
#         anagrams[sorted_str].append(s)
    
#     # Return the grouped anagrams as a list of lists
#     return list(anagrams.values())

# # Example usage
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(strs))


# #2
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # An anagram has the same characters with the same frequencies
#         return sorted(s) == sorted(t)

# def main():
#     # Input function to read strings
#     s = input("Enter the first string: ")
#     t = input("Enter the second string: ")

#     # Create an instance of the Solution class
#     solution = Solution()

#     # Check if the two strings are anagrams
#     result = solution.isAnagram(s, t)

#     # Print the result
#     if result:
#         print(f'"{s}" and "{t}" are anagrams.')
#     else:
#         print(f'"{s}" and "{t}" are not anagrams.')

# if __name__ == "__main__":
#     main()
