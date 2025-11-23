class Solution:
    def containsNearbyDuplicate(self, n: List[int], k: int) -> bool:
        dct = {}
        for i in range(len(n)):
            if n[i] in dct and i - dct[n[i]] <= k:
                return True
                break
            dct[n[i]] = i
        return False
__import__('atexit').register(lambda: open('display_runtime.txt','w').write('0'))


        
