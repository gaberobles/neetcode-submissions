class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        
        for token in tokens:
            print(stack)
            if token in operators:
                if token == '+':
                    o1 = stack.pop()
                    o2 = stack.pop()
                    print(o1, "+", o2)
                    stack.append(o2 + o1)
                elif token == '-':
                    o1 = stack.pop()
                    o2 = stack.pop()
                    print(o1, "-", o2)
                    stack.append(o2 - o1)
                elif token == '*':
                    o1 = stack.pop()
                    o2 = stack.pop()
                    print(o1, "*", o2)
                    stack.append(o2 * o1)
                else:
                    o1 = stack.pop()
                    o2 = stack.pop()
                    print(o1, "//", o2)
                    stack.append(int(o2 / o1))
            else:
                stack.append(int(token))
        
        return stack[-1]