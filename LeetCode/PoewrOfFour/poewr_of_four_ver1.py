import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 0 : return False
        answer = math.log10(num)/math.log10(4)
        if int(answer) == answer :
            return True
        else :
            return False


t = Solution()
print(t.isPowerOfFour(-2147483648))
