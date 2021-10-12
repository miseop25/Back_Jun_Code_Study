import math

class PersonInfo :
    def __init__(self, name):
        self.child = set()
        self.name = name
        self.parent = ""
        self.price = 0
        self.pArr = []

class MainTree :
    def __init__(self, enroll, referral, seller, amount):
        self.enroll = enroll
        self.referral = referral
        self.seller = seller
        self.amount = amount 

        self.center = PersonInfo("Center")

        self.personDict = dict()
        self.answer = []

    
    def makePersonDict(self) :
        for p in self.enroll :
            self.personDict[p] = PersonInfo(p)
    
    def makeTree(self) :
        for i, val in enumerate(self.referral) :
            name = self.enroll[i]
            if val == "-" :
                self.center.child.add(name)
                continue
            self.personDict[val].child.add(name)
            self.personDict[name].parent = val
    
    def setPrice(self) :
        for name, am in zip(self.seller,self.amount) :
            tPer = self.personDict[name]
            basePrice = am * 100
            upPrice = basePrice
            while upPrice != 0 :
                upPrice = self.calcPrice(basePrice)
                self.personDict[tPer.name].price += (basePrice - upPrice)
                basePrice = upPrice
                if tPer.parent == "" :
                    self.center.price += basePrice
                    break
                else :
                    tPer = self.personDict[tPer.parent]
    
    def calcPrice(self, upPrice) :
        upPrice = upPrice * 0.1 
        if upPrice < 1 :
            upPrice = 0
        else :
            upPrice = math.floor(upPrice)
        return upPrice

    def getAnswer(self) :
        self.makePersonDict()
        self.makeTree()
        self.setPrice()

        for p in self.enroll :
            self.answer.append(self.personDict[p].price)
        return self.answer

def solution(enroll, referral, seller, amount):
    answer = []
    mt = MainTree(enroll,referral, seller, amount)
    answer = mt.getAnswer()
    return answer


e = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
r = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
s = ["young", "john", "tod", "emily", "mary"]
a = [12, 4, 2, 5, 10]
print(solution(e,r,s,a))