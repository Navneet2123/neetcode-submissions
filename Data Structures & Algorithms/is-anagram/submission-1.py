class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        data=dict()
        if len(s)!=len(t): return False
        for i in range(len(s)):
            data[s[i]]=1+data.get(s[i],0)
            data[t[i]]=data.get(t[i],0)-1
        for s in data:
            if data[s]!=0:
                return False
        return True