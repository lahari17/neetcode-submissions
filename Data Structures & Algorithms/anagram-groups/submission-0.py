class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen1={}
        for s in strs:
            skey= "".join(sorted(s))
            seen1[skey] = seen1.get(skey, [])+[s]

        seenlist=[]
        for k,v in seen1.items():
            seenlist=seenlist+[v]
        return seenlist
