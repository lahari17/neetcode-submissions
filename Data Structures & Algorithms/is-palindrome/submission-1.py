class Solution:
    def isPalindrome(self, s: str) -> bool:
        word =""
        for ch in s:
            if ch.isalnum():
                word = word + ch
        word = word.lower()
        n=len(word)
        left = 0
        right = n-1
        while left<right:
            if word[left] != word[right]:
                return False
            left=left+1
            right= right -1
        return True
            