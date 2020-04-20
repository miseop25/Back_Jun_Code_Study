import sys
import collections
input = sys.stdin.readline

def soluction(array, N , M) :
    ans_list = []
    dp = collections.deque([[0,0, array[0][0]]])

    while dp :
        x, y, candy = dp.popleft()
        if x == N-1 and y == M-1 :
            ans_list.append(candy)
            continue
        if x+1 < N :
            x1 = x+1
            y1 = y
            c1 = candy + array[x1][y1]
            dp.append([x1, y1, c1])
        if y + 1 < M :
            x2 = x
            y2 = y + 1
            c2 = candy + array[x2][y2]
            dp.append([x2, y2, c2])
        if x + 1 < N and y + 1 < M :
            x3 = x + 1
            y3 = y + 1
            c3 = candy + array[x3][y3]
            dp.append([x3, y3, c3])
    ans_list = list(set(ans_list))
    print(ans_list)
    return max(ans_list)
        


N, M = map(int, input().split(" "))
candy_map = []
for i in range(N) :
    candy_map.append(list(map(int, input().split(" "))))

print(soluction(candy_map, N ,M ))
