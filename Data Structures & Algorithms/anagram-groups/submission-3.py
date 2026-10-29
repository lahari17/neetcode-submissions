class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group={}
        for word in strs:
            count = [0]*26
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            key = tuple(count)
            if key in group:
                group[key].append(word)
            else:
                group[key]=[word]

        return list(group.values())

#Time = O(nk)
#Space= O(nk)

            

            


