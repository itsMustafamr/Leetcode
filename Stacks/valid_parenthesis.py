class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #create an empty stack
        # a dictionary or hashmap
        match_element = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in match_element:
                if stack and stack[-1] == match_element[char]:
                    stack.pop()
                else:
                    return False
            
            else: 
                stack.append(char)
        # return True if not stack else False
        return not stack
        #Stack should be empty if all brackets are matched
    
s = "{[()()]}"
solution = Solution()
print(solution.isValid(s))

# other way of doing it
# for char in s:
#             if char in matching_brackets.values():  # Opening brackets
#                 stack.append(char)
#             elif char in matching_brackets.keys():  # Closing brackets
#                 if stack == [] or matching_brackets[char] != stack.pop():
#                     return False
#             else:
#                 return False  # In case of any invalid character
                
#         return stack == []
            