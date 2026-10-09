class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l1=0
        l2=0
        l3=0
        seen=set()
        for l2 in range(len(s)):
            if s[l2] not in seen:
                seen.add(s[l2])
            else:
                while s[l2] in seen:
                    seen.remove(s[l1])
                    l1=l1+1
                seen.add(s[l2])
            l3=max(l3,l2-l1+1)
        return l3




            