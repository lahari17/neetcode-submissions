class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        res=0
        l=0
        window=0
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            while (r-l+1)-max(count.values())>k:
                count[s[l]]= count[s[l]]-1
                l=l+1
            res=max(res,r-l+1)
        return res

#Time - O(n)
#space-O(m)




        