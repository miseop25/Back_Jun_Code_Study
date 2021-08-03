import Foundation

class SupplyMoney {
    let price:Int
    let money:Int
    let count:Int
    
    var answer:Int64
    
    init(price:Int, money:Int, count:Int) {
        self.price = price
        self.money = money
        self.count = count

        self.answer = -1
    }

    func getAnswer() -> Int64
    {
        var payment:Int64 = 0
        for i in 1...self.count {
            payment += Int64(self.price * i)
        }
        if (self.money >= payment) {
            return 0
        }
        answer = payment - Int64(self.money)
        return answer
    }
    
    
}


func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var answer:Int64 = -1

    let sp = SupplyMoney(price: price,money: money, count: count)
    answer = sp.getAnswer()
    
    return answer
}

print(solution(3, 20, 4))

