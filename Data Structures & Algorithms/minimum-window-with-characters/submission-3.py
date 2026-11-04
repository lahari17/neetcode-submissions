class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        freq_t = {}
        for i in range(len(t)):
            freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        need = len(freq_t)
        left = 0
        window = {}
        have = 0 

        min_length = float("inf")
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if (s[right] in freq_t) and (window[s[right]] == freq_t[s[right]]):
                have = have +1

            while have==need:
                length = right - left +1

                if length < min_length:
                    min_length = length
                    result = s[left: left+length]

                if ((s[left] in freq_t) and (window[s[left]] == freq_t[s[left]])):
                    have = have - 1
                
                window[s[left]]=window[s[left]]-1
                left = left +1
        return "" if min_length==float("inf") else result


                



    