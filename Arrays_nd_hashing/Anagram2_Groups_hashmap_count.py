from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            # Create a count of each character
            count = [0] * 26  # Assuming the input strings contain only lowercase letters a-z
            for char in s:
                count[ord(char) - ord('a')] += 1
                #this is finding diff in ascii values of charecters
            
            # Use the tuple of counts as the key
            key = tuple(count)
            anagrams[key].append(s)
        
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
