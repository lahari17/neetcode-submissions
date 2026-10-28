class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #bruteforce= sorted(s) and sorted(t) and compare, time = O(nlogn)
        sdict = {}
        tdict = {}
        for schar in s:
            sdict[schar] = sdict.get(schar,0) + 1
        for tchar in t:
            tdict[tchar] = tdict.get(tchar,0) + 1

        if sdict == tdict:
            return True
        return False

#Time = O(n)
#Space=O(n)