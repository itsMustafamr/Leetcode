class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                b, a = stack.pop(), stack.pop()# pop second, then first
                stack.append(a - b)# subtract in correct order
            elif c == "*":
                stack.append(stack.pop() * stack.pop())        
            elif c == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))  # truncate towards zero
            else:
                stack.append(int(c)) 

        return stack[0]
