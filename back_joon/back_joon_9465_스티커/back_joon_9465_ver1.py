import sys
input = sys.stdin.readline


def soluction(array, width) :
    answer = 0 
    dx = [-1, 1 , 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(2) :
        for j in range(width) :
            if array[i][j] == 0 :
                continue
            else :
                buf = array[i][j]
                check = True
                for k in range(4) :
                    x = j + dx[k]
                    y = i + dy[k]
                    if x >= 0 and x < width and y >= 0 and y < 2 :
                        if array[y][x] > buf :
                            check = False
                if check :
                    for k in range(4) :
                        x = j + dx[k]
                        y = i + dy[k]
                        if x >= 0 and x < width and y >= 0 and y < 2 :
                            array[y][x] = 0
    for ans in array :
        answer += sum(ans)
    return answer
def soluction2(array, width) :
    answer = 0 
    dx = [-1, 1 , 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(1, 0, -1) :
        for j in range(width) :
            if array[i][j] == 0 :
                continue
            else :
                buf = array[i][j]
                check = True
                for k in range(4) :
                    x = j + dx[k]
                    y = i + dy[k]
                    if x >= 0 and x < width and y >= 0 and y < 2 :
                        if array[y][x] > buf :
                            check = False
                if check :
                    for k in range(4) :
                        x = j + dx[k]
                        y = i + dy[k]
                        if x >= 0 and x < width and y >= 0 and y < 2 :
                            array[y][x] = 0
    for ans in array :
        answer += sum(ans)
    return answer


T = int(input())
for _ in range(T) :
    sticker = []
    n = int(input())
    for i in range(2) :
        buf = list(map(int, input().split(" ")))
        sticker.append(buf)
    print(soluction(sticker, n))
    print(soluction2(sticker, n))
    