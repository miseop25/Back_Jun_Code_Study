class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        c1 = word.upper()
        c2 = word.lower()
        c3 = word.capitalize()
        if c1 == word or c2 == word or c3 == word :
            return True
        else :
            return False





a = Solution()
print( a.detectCapitalUse("g"))