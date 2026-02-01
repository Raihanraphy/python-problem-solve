class Solution:
    def palindromePairs(self,words)->list:
        cnt=len(words)
        lens=set()
        hashmap={}
        ans=[]
        def ispalindrome(s,l,r):
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        for i in range(cnt):
            lens.add(len(words[i]))
            hashmap[words[i]]=i
        for i in range(cnt):
            rev=words[i][::-1]
            l=len(rev)
            print(rev)
            if rev in hashmap and hashmap[rev]!=i:
                ans.append([i,hashmap[rev]])
            for j in lens:
                if j>=l:
                    continue
                if rev[:j] in hashmap and ispalindrome(rev,j,l-1):
                    ans.append([hashmap[rev[:j]],i])
                if rev[l-j:] in hashmap and ispalindrome(rev,0,l-j-1):
                    ans.append([i,hashmap[rev[l-j:]]])
        return ans
