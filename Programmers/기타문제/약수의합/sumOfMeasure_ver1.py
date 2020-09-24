class Measure :
    def __init__(self, num) :
        self.measure = set()
        if num != 0 :
            self.measure.add(1)
        else :
            self.measure.add(0)
        self.getMeasure(num)

    
    def getMeasure(self,n) :
        self.measure.add(n)
        for i in range(2, n//2 + 1) :
            v, r = divmod(n, i) 
            if r == 0 :
                if v not in self.measure :
                    self.getMeasure(v)
    
    def sumOfMeasure(self) :
        return sum(self.measure)


def solution(n) :
    answer = 0
    m = Measure(n)
    answer = m.sumOfMeasure()
    return answer

print(solution(1))