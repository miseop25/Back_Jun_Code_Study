import sys
import itertools
input = sys.stdin.readline

def soluction(num, n, S) :
    array = itertools.combinations(num, n)
    answer = 0
    for i in array :
        temp = sum(i)
        if temp == S :
            answer += 1
    return answer


if __name__ == "__main__":
    N, S = map(int,input().split(" "))
    num = list(map(int, input().split(" ")))
    answer = 0
    for i in range(1, N+1) :
        answer += soluction(num, i, S)
    print(answer)



