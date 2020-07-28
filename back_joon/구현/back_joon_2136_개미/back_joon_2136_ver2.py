import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, (input().split(" ")))
    ant = dict()
    for i in range(1, N+1) :
        buf = int(input())
        if buf < 0 :
            val = abs(buf)
        else :
            val = L - buf
        ant[i] = [val, buf]
    time = sorted(ant.items(), key= lambda x: x[1][0] )

    comp = time[-1]
    for t in time[: -1] :
        if abs(t[1][1]) > comp[1][1] and t[1][1] < comp[1][1] :
            comp = t

    answer = str(comp[0]) + " " + str(time[-1][1][0])
    print(answer)
