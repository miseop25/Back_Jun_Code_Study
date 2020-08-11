class Solution:
    def titleToNumber(self, s: str) -> int:
        answer = 0
        lenght = len(s) - 1 
        for i in s :
            if lenght == 0 :
                answer += (ord(i)-64)
            else :
                answer += (ord(i)-64)*(26**lenght)
            lenght -= 1
        return answer

s = Solution()
print(s.titleToNumber("ZY"))
print(s.titleToNumber("AA"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("AAA"))