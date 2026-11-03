class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        s1_count = [0] * 26
        window_count = [0] * 26

        # Count characters in s1 and first window
        for i in range(n):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1

        # Count how many character frequencies match
        matches = sum(
            s1_count[i] == window_count[i] for i in range(26)
        )

        left=0
        # Slide the window
        for right in range(n, len(s2)):

            if matches == 26:
                return True

            # Add incoming character
            j = ord(s2[right]) - ord('a')

            window_count[j] += 1

            if window_count[j] == s1_count[j]+1:
                matches -= 1

            if window_count[j] == s1_count[j]:
                matches += 1

            # Remove outgoing character
            j = ord(s2[left]) - ord('a')

            window_count[j] -= 1

            if window_count[j] == s1_count[j]-1:
                matches -= 1

            if window_count[j] == s1_count[j]:
                matches += 1
            left = left + 1
        if matches==26:
            return True
        else:
            return False
