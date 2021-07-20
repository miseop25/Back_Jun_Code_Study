class Divisor :
    def __init__(self,left, right):
        self.left = left
        self.right = right 
        self.answer = 0

    def getDivisor(self,num) :
        result = set()
        if num == 1 :
            result.add(num)
            return result
        for i in range(1, int(num//2)+1 ) :
            if num % i == 0 :
                result.add(i)
                result.add(num//i)
        return result
    
    def getAnswer(self) :
        for i in range(self.left, self.right + 1) :
            divisor_Set = self.getDivisor(i)
            if len(divisor_Set)%2 == 0 :
                self.answer += i
            else :
                self.answer -= i
        
        return self.answer

def solution(left, right):
    d = Divisor(left,right)
    answer = d.getAnswer()
    return answer