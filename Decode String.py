class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        index = 0
        while index < len(s):
            c = s[index]
            if c.isdigit():
                num = 0
                while s[index].isdigit():
                    num *= 10
                    num += int(s[index])
                    index += 1
                stack.append(num)
                continue
            if c == ']':
                phrase = []
                while stack and stack[-1] != '[':
                    phrase.append(stack.pop())
                stack.pop()
                multiplier = stack.pop()
                stack.append("".join(reversed(phrase)) * multiplier)
            else:
                stack.append(c)
            index += 1
        res = "".join(stack)
        return res
