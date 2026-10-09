class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)

        for i in range(len(s2) - n + 1):
            substring = s2[i:i + n]

            if self.get_counts(substring) == self.get_counts(s1):
                return True

        return False

    def get_counts(self, s):
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        return count