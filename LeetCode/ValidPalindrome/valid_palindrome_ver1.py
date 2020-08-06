class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        s = s.lower()
        for i in s :
            if (i >= "a" and i <= "z") or (i >= "0" and i <= "9") :
                result += i
        if result == result[::-1] :
            return True
        else :
            return False
         