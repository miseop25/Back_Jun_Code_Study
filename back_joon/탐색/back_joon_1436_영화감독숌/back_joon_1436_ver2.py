def soluction(num) :
    answer = set()
    answer.add(666)
    value = 666
    i = 0
    while len(answer) < num :
        i += 1
        value += 1000
        answer.add(value)
        if i%10 == 6 :
            temp = str(value)
            check = temp[temp.find("666") + 3: ]
            st = value - int(check)
            ed = st + 10**len(check)
            for j in range(st, ed) :
                answer.add(j)
    result = sorted(answer)
    return result[num-1]
    

if __name__ == "__main__":
    N = int(input())
    print(soluction(N))
