import sys
input = sys.stdin.readline

def soluction(a,b) :
    price = 0
    if a == 1 :
        price += 500
    elif a >=2 and a <=3 :
        price += 300
    elif a >= 4 and a <= 6 :
        price += 200
    elif a >= 7 and a <= 10 :
        price += 50
    elif a >= 11 and a<= 15 :
        price += 30
    elif a<=21 and a != 0 :
        price += 10
    
    money = 512 
    t = 1

    for i in range(1, 6) :
        if b <= t and b != 0 :
            price += money
            return str(price*10000)
            
        t += i**2
        money = money//2
    return str(price*10000)

if __name__ == "__main__":
    case = int(input())
    for _ in range(case) :
        a, b = map(int, input().split(" "))
        print(soluction(a,b))
    
        