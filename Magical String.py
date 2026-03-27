s = '1221121221221121122'
s = [c == '1' for c in s]
j = 12
while len(s) < 10 ** 5:
    s += [not s[-1]]
    if not s[j]:
        s += [not s[-2]]
    j += 1

solution = [0]
for b in s:
    solution += [solution[-1] + int(b)]

class Solution:
    def magicalString(self, n: int) -> int:
        return solution[n]
