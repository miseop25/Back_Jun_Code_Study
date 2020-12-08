import sys
input = sys.stdin.readline

def checkAB(i,j) :
    if i == 1 :
        a = 0
        b = j
    elif i == 2 :
        a = j
        b = Y
    elif i == 3 :
        a = 0
        b = j
    elif i == 4 :
        a = X
        b = j
    return a,b


if __name__ == "__main__":
    X, Y = map(int, input().split(" "))
    p = int(input())
    store = []
    for _ in range(p) :
        temp = list(map(int, input().split(" ")))
        store.append(temp)
    dX, dY = map(int, input().split(" "))
    dX,dY = checkAB(dX, dY)

    length = []
    for i, j in store :
        a,b = checkAB(i,j)
        
        toZero = dX + dY + a + b
        toXY = (X- a) + (X - dX) + (Y - b) + (Y - dY)
        length.append(min(toXY, toZero))
    
    answer = sum(length)
    print(answer)