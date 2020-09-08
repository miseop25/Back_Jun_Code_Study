import sys
input = sys.stdin.readline

class JoungRestaurant :
    def __init__(self) :
        self.normal = dict()
        self.special = dict()
        self.service = set()

        self.normalPrice = 0
        self.totalPrice = 0

        self.serviceCnt = 0
        self.specialCnt = 0
    
    def setMenu(self) :
        A, B, C = map(int, input().split(" "))
        for _ in range(A) :
            menu, price = input().rstrip().split(" ")
            self.normal[menu] = int(price)
        for _ in range(B) :
            menu, price = input().rstrip().split(" ")
            self.special[menu] = int(price)
        for _ in range(C) :
            menu = input().rstrip()
            self.service.add(menu)
    
    def getOrder(self) :
        N = int(input())
        for _ in range(N) :
            menu = input().rstrip()
            if menu in self.normal :
                self.normalPrice += self.normal[menu]
                self.totalPrice += self.normal[menu]
            elif menu in self.special :
                self.totalPrice += self.special[menu]
                self.specialCnt += 1
            else :
                self.serviceCnt += 1
    
    def checkOrder(self) :
        if self.specialCnt > 0 and self.normalPrice < 20000 :
            return "No"
        if self.serviceCnt > 1 :
            return "No"
        elif self.serviceCnt == 1 and self.totalPrice < 50000 :
            return "No"
        return "Okay"




if __name__ == "__main__":
    jung = JoungRestaurant()
    jung.setMenu()
    jung.getOrder()
    print(jung.checkOrder())