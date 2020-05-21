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
    case1 = list(itertools.product(A, B))
    case2 = list(itertools.product(C, D))
    result1 = dict()
    result2 = dict()
    for i in range(len(case1)) :
        s1 = sum(case1[i])
        s2 = sum(case2[i])
        if s1 in result1 :
            result1[s1] += 1
        else:
            result1[s1] = 1
        if s2 in result2 :
            result2[s2] += 1
        else:
            result2[s2] = 1
    
    for k in result1.keys() :
        if -k in result2 :
            answer += result2[-k]*result1[k]
    return answer

if __name__ == "__main__":
    n = int(input())
    print(soluction(n))