import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    word = ""
    check_error = 0
    enter = 0
    while True :
        buf = input()
        if buf != "\n" :
            word += buf
            enter += 1
        else :
            break
    for j in word :
        if j == "#" :
            check_error += 1
    length = len(word) - enter
    rate = round(((length - check_error)/length)*100, 1)
    rate = str(rate)
    if rate[-1] == "0" :
        rate = rate[: -2]
    rate += "%."
    print("Efficiency ratio is", rate)
