import sys
input = sys.stdin.readline

numDict = {1: [1],
        2: [2,4,8,6],
        3: [3,9,7,1],
        4: [4,6],
        5: [5], 6: [6],
        7: [7,9,3,1],
        8: [8,4,2,6],
        9: [9,1],
        0: [10]
        }

def soluction() :
    a, b = map(int, input().split(" "))
    k = int(str(a)[-1])
    v = b%(len(numDict[k])) - 1

    return numDict[k][v]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T) :
        print(soluction())

    