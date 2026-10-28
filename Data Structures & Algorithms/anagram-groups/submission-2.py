class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for i in strs:
            anag = "". join(sorted(i))
            if anag in group:
                group[anag].append(i)
            else:
                group[anag]=[i]
        return [x for x in group.values()]