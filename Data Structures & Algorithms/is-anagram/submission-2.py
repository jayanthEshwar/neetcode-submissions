class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}
        for i in range(0,len(s)):
            freq1[s[i]]=freq1.get(s[i],0)+1
        for i in range(0,len(t)):
            freq2[t[i]]=freq2.get(t[i],0)+1
        
        if freq1==freq2:
            return True
        else:
            return False
