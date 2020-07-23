bracket = input().rstrip()

total = [0 for i in range(len(bracket))]
small = []
big = []
check = False

for i in range(len(bracket)) :
    if bracket[i] == "(" :
        small.append(i)
    elif bracket[i] == "[" :
        big.append(i)
    elif bracket[i] == ")" :
        if not small :
            check = True
            break
        st = small.pop()
        if big :
            if st < big[-1] :
                check = True
                break
        temp = 0
        for j in range(st, i) :
            temp += total[j]
            total[j] = 0
        if temp == 0 :
            total[i] = 2
        else :
            total[i] = 2*temp
    elif bracket[i] == "]" :
        if not big :
            check = True
            break
        st = big.pop()
        if small :
            if st < small[-1] :
                check = True
                break
        temp = 0
        for j in range(st, i) :
            temp += total[j]
            total[j] = 0
        if temp == 0 :
            total[i] = 3
        else :
            total[i] = 3*temp
    else :
        check = True
        break
if small or big or sum(total) == 0 or check:
    print(0)
else :
    print(sum(total))