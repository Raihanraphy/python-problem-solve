class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                a = num[:i]
                b = num[i:j]

                if (a.startswith('0') and len(a) > 1) or (b.startswith('0') and len(b) > 1):
                    continue

                x, y = int(a), int(b)
                k = j

                while k < n:
                    s = str(x + y)
                    if not num.startswith(s, k):
                        break
                    k += len(s)
                    x, y = y, x + y

                if k == n:
                    return True

        return False
