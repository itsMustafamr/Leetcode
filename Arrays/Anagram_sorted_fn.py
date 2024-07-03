class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        return s == t

#here it is just a word so we don't have to change it to split letter.

sol = Solution()
# a = []
# b = []
# inp_1 = input("enter 2 strings s and t", a) 
# inp_2 = input("enter 2 strings s and t", b)
# print(inp_1,inp_2)
s = input("Enter the first string: ")
t = input("Enter the second string: ")

result = sol.isAnagram(s, t)
print("result", result)