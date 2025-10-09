class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2 = version1.split('.'), version2.split('.')
        while len(v1) > len(v2):
            v2.append(0)
        while len(v2) > len(v1):
            v1.append(0)   

        for i in range(len(v1)):
            i1,i2 = int(v1[i]), int(v2[i])
            if i1 < i2:
                return -1
            elif i2 < i1:
                return 1
        return 0
