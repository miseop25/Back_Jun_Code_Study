import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        answer = math.log10(abs(num))/math.log10(4)

        if int(answer) == answer :
            return True
        else :
            return False


t = Solution()
print(t.isPowerOfFour(-2147483648))
