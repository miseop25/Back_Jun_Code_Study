class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0 : 
            isNegative = True
        x = str(abs(x))
        if isNegative :
            answer = int(x[::-1])*-1
        else :
            answer = int(x[::-1])
        if abs(answer) >= 2**31 :
            return 0
        return answer