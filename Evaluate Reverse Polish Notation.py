class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    stack.append(stack.pop()+stack.pop())
                case '-':
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(second-first)
                case '*':
                    stack.append(stack.pop()*stack.pop())
                case '/':
                    first = stack.pop()
                    second = stack.pop()
                    stack.append(trunc(second/first))
                case _:
                    stack.append(int(token))
        return stack[0]
