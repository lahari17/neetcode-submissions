class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest =0
        left =0
        seen={}
        for right in range(len(s)):
            seen[s[right]]= seen.get(s[right], 0) +1
            window_length = right - left + 1
            max_val = max(seen.values())
            replacements = window_length - max_val
            while replacements > k:
                seen[s[left]] = seen[s[left]] - 1
                left = left +1
    
                window_length = right - left + 1
                max_val = max(seen.values())
                replacements = window_length - max_val
            longest = max(longest, window_length)
        return longest



             


