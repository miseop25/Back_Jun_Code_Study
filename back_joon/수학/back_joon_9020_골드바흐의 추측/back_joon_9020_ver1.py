import sys
input = sys.stdin.readline

def getPrimeNumber() :
    answer = dict()
    prime = [True for i in range(10001)]
    for i in range(2, 10001) :
        if prime[i] :
            answer[i] = True
            for j in range(i*2, 10001, i) :
                prime[j] = False
    return answer

num = getPrimeNumber()

def soluction() :
    n = int(input())
    result = []
    for i in range(n-1, n//2 - 1, -1) :
        if i in num and (n-i) in num :
            result.append([i, n-i])

    result = sorted(result, key= lambda x: (abs(x[0]- x[1])))
    ans = sorted(result[0])
    return str(ans[0]) + " " + str(ans[1])

if __name__ == "__main__":
    c = int(input())
    for _ in range(c) :
        print(soluction())





