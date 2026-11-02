class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length= 0
        seen = set()
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                length = max(length, len(seen))
            else:
                while(s[left]!=s[right]):
                    seen.remove(s[left])
                    left = left + 1
                seen.remove(s[left])
                left = left+1
                seen.add(s[right])
                length = max(length, len(seen))

        return length
                    






