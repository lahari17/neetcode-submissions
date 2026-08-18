class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1=strs[0]
        for i in range(1, len(strs)):
            for j in range(0, len(str1)):
                if j== len(strs[i]) or str1[j]!=strs[i][j]:
                    str1=str1[0:j]
                    break
        return str1
