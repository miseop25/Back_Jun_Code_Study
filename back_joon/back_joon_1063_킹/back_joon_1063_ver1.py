A, B, N = map(str, input().split(" "))
king = [A[0], A[1]]
stone = [B[0], B[1]]


for i in range(int(N)) :
    move = str(input())
    x = []
    y = []

    if move == "R" :
        if king[0] != "H" :
            king[0] = chr(ord(king[0]) + 1)
            x.append(1)
    elif move == "L" :
        if king[0] != "A" :
            king[0] = chr(ord(king[0]) - 1)
            x.append(1)
    elif move == "B" :
        if king[1] != "1" :
            king[1] = str( int(king[1]) - 1)
            y.append(-1)
    elif move == "T":
        if king[1] != "8" :
            king[1] = str(int(king[1]) + 1)
            y.append(1)
    elif move == "RT" :
        if king[0] != "H" or king[1] != "8" :
            king[1] = str(int(king[1]) + 1)
            king[0] = chr(ord(king[0]) + 1)
            x.append(1)
            y.append(1)
    elif move == "LT" :
        if king[0] != "A" or king[1] != "8" :
            king[1] = str(int(king[1]) + 1)
            king[0] = chr(ord(king[0]) - 1)
            x.append(-1)
            y.append(1)
    elif move == "RB" :
        if king[0] != "H" or king[1] != "1" :
            king[1] = str(int(king[1]) - 1)
            king[0] = chr(ord(king[0]) + 1)
            x.append(1)
            y.append(-1)
    elif move == "LB" :
        if king[0] != "A" or king[1] != "1" :
            king[1] = str(int(king[1]) - 1)
            king[0] = chr(ord(king[0]) - 1)
            x.append(-1)
            y.append(-1)
    #  킹이 돌의 위치로 가는 경우
    if king[0] == stone[0] and king[1] == stone[1] :
        if y :
            stone[1] = str(int(stone[1]) + y[0])
        if x :
            stone[0] = chr(ord(stone[0]) + x[0])
        # 돌이 체스판 밖으로 나가는 경우
        if stone[0] < "A" or stone[0] > "H" or stone[1] < "1" or stone[1] > "8" :
            if y :
                stone[1] = str(int(stone[1]) - y[0])
                king[1] = str(int(king[1]) - y[0])
            if x :
                stone[0] = chr(ord(stone[0]) - x[0])
                king[0] = chr(ord(king[0]) - x[0])
print("".join(king))
print("".join(stone))
