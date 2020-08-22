import sys
input = sys.stdin.readline

def soluction() :
    num = int(input())
    result = []
    for _ in range(num) :
        sc1, sc2 = map(int, input().split(" "))
        result.append([sc1, sc2])
    result = sorted(result, key= lambda x: x[0]) 

    answer = 1
    for i in range(1, num) :
        if result[i-1][1] > result[i][1] :
            answer += 1
    return answer


if __name__ == "__main__":
    N = int(input())
    for _ in range(N) :
        print(soluction())
