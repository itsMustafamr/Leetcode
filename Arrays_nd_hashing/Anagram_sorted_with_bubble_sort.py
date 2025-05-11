class Solution:
    def bubble_sort(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i in range(n):
            for j in range(0, n-i-1):
                if s[j] > s[j+1]:
                    s[j], s[j+1] = s[j+1], s[j]
        return ''.join(s)

    def isAnagram(self, s: str, t: str) -> bool:
        # Sort both strings using bubble sort
        sorted_s = self.bubble_sort(s)
        sorted_t = self.bubble_sort(t)
        
        # Check if the sorted versions of the strings are equal
        return sorted_s == sorted_t

# Create an instance of the Solution class
solution = Solution()

# Take input from the user for the two strings
s = input("Enter the first string: ")
t = input("Enter the second string: ")

# Check if the strings are anagrams and print the result
result = solution.isAnagram(s, t)
print(f"Are '{s}' and '{t}' anagrams? {result}")
