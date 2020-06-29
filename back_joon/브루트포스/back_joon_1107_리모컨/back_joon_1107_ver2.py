import itertools
def soluction(N, num) :
    if N == 100 :
        return 0
    if len(num) == 0 :
        return abs(100 - N)
    ansList = [abs(N- 100)]
    nStr = str(N)
    case = []
    for _ in range(len(nStr) + 1) :
        case.append(num)

    def check() :
        a = []
        if case :
            temp = list(itertools.product(*case))
            for i in temp :
                buf = "".join(i)
                a.append(abs(N - int(buf)) + len(buf) )
            case.pop()
        if a :
            ansList.append(min(a))

    for _ in range(3) :
        check()

    return min(ansList)

if __name__ == "__main__":
    while True :
        N = int(input())
        num = [str(i) for i in range(10)]
        M = int(input())
        if M != 0 :
            dosentWork = list(map(int, input().split(" ")))
            for i in dosentWork :
                num.remove(str(i))
        print(soluction(N, num))
        break
