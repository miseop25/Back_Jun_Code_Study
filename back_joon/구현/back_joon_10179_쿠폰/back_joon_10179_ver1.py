class Coupons :
    def __init__(self, tastCase):
        self.tc = tastCase
    
    def applyCoupon(self, price) :
        applyPrice = '${0:0.2f}'.format(price*0.8)
        print(applyPrice)
    
    def getAnswer(self) :
        for _ in range(self.tc) :
            price = float(input().strip(""))
            self.applyCoupon(price)


if __name__ == "__main__" :
    s = Coupons(int(input().strip("")))
    s.getAnswer()


