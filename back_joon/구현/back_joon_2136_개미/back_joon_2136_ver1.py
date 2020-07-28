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
        ant[str(i)] = str(val)
    result = sorted(ant.items(), key= lambda x: -int(x[1]) )
    answer = " ".join(result[0])
    print(answer)
