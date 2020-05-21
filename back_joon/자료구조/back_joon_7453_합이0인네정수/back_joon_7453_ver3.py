import sys
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

    case1 = dict()
    for i in range(N) :
        for j in range(N) :
            temp = A[i] + B[j]
            if temp in case1 :
                case1[temp] += 1
            else :
                case1[temp] = 1
    for i in range(N) :
        for j in range(N) :
            temp = -(C[i] + D[j])
            if temp in case1 :
                answer += case1[temp]

    return answer

if __name__ == "__main__":
    n = int(input())
    print(soluction(n))