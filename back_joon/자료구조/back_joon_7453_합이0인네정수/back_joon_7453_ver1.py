import sys
import itertools
input = sys.stdin.readline

def soluction(N) :
    answer = 0
    A = []
    B = []
    C = []
    D = []
    for _ in range(N) :
        a1,b1,c1,d1 = map(int, input().split(" "))
        A.append(a1)
        B.append(b1)
        C.append(c1)
        D.append(d1)
    result = list(itertools.product(A, B, C, D))
    for i in result :
        if sum(i) == 0 :
            answer += 1

    return answer

if __name__ == "__main__":
    n = int(input())
    print(soluction(n))