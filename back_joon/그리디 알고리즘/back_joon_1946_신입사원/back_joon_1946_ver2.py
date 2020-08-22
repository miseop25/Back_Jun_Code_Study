import sys
input = sys.stdin.readline

def soluction() :
    num = int(input())
    result = []
    for _ in range(num) :
        sc1, sc2 = map(int, input().split(" "))
        result.append([sc1, sc2])
    paper = sorted(result, key= lambda x: x[0]) 
    answer = 1
    comp = paper[0][1]
    for i in range(1, num ) :
        if paper[i][1] < comp :
            answer += 1
            comp = paper[i][1]
    return answer


if __name__ == "__main__":
    N = int(input())
    for _ in range(N) :
        print(soluction())
