def soluction(X, y) :
    Z = int(100*Y/X) + 1

    n = 100 - Z 
    if n == 0 or Z >= 100:
        return -1
    val = X*Z - Y*100 
    v, r = divmod(val, n)
    if r == 0 :
        answer = v
    else :
        answer = v + 1
    return answer

if __name__ == "__main__":
    while True :
        try :
            X, Y = map(int, input().split(" "))
            print(soluction(X, Y))
        except :
            break

    

