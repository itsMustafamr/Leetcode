from typing import List

    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # )( this is invalid 
        # for n = 3, 3 open, 3 close
        # close < open
        # only add open parenthesis if open < n
        # only add closing parenthesis if close < open
        # valid if and only if open == closed == n

        stack = []
        res = [] 

        def backtrack(openN, closedN): # we are doing it recursively
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res







        