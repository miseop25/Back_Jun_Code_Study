if __name__ == "__main__":
    n, T = map(int, input().split(" "))
    num = list(map(int, input().split(" ")))
    answer = 0
    for i, v in enumerate(num) :
        if T > 0 :
            T -= v
            answer += 1
        else :
            break
    if T >= 0 :
        print(answer)
    else :
        print(answer-1)