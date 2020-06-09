import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    num = dict()
    num[1] = [[1,1,1,1,1,1,1,1,1,1], 10]
    num[2] = [[10,9,8,7,6,5,4,3,2,1], 55]
    for i in range(3, 65) :
        cnt = num[i-1][1]
        num[i] = [[]]
        for j in num[i-1][0] :
            num[i][0].append(cnt)
            cnt -= j
        num[i].append(sum(num[i][0]))
    for _ in range(T) :
        temp = int(input())
        print(num[temp][1])
    