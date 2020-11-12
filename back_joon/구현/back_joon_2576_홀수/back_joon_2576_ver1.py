if __name__ == "__main__":
    numOdd = []
    oddTotal = 0
    for _ in range(7) :
        temp = int(input())
        if temp%2 == 1 :
            oddTotal += temp
            numOdd.append(temp)
    if numOdd :
        print(oddTotal)
        print(min(numOdd))
    else :
        print(-1)