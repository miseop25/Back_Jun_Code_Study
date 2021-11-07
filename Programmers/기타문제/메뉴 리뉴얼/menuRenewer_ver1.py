from itertools import combinations 

class Menu :
    def __init__(self, orders, course):
        self.orders = orders
        self.course = course

        self.newCourse = dict()
        for i in course :
            self.newCourse[i] = dict()
        self.answer = []
    
    def makeNewCourse(self) :
        for o in self.orders :
            temp = list(o)
            for i in self.course :
                cList = list(combinations(temp, i))
                self.addDict(cList, i)
    
    def addDict(self, cArr, baseLen) :
        for a in cArr :
            t = list(a)
            t.sort()
            strKey = "".join(t)
            if strKey in self.newCourse[baseLen] :
                self.newCourse[baseLen][strKey] += 1
            else :
                self.newCourse[baseLen][strKey] = 1
    
    def getAnswer(self) :
        self.makeNewCourse()
        for i in self.course :
            if len(self.newCourse[i]) == 0 :
                continue
            temp = sorted(self.newCourse[i].items(), key = lambda x : -x[1])
            maxLen = temp[0][1]
            if maxLen == 1 :
                continue
            for c in temp :
                if c[1] == maxLen :
                    self.answer.append(c[0])

        return sorted(self.answer)




def solution(orders, course):
    answer = []
    s= Menu(orders, course)
    answer = s.getAnswer()
    return answer

o = ["XYZ", "XWY", "WXA"]
c = [2,3,4]
print(solution(o,c))