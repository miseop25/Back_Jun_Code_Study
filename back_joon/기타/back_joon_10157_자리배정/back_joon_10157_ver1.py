W, H = map(int, input().split(" "))
K = int(input())

board = [ [0 for _ in range(W)] for _ in range(H)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
d = 0 
i = 0 
j = 0
cnt = 1
check = True
board[0][0] = 1
if W*H < K :
    cnt = K
    check = False
while cnt != K :
    n_i = i + direction[d][0]
    n_j = j + direction[d][1]
    if n_i < H and n_i >= 0 and n_j < W and n_j >= 0 : 
        if board[n_i][n_j] == 0 :
            board[n_i][n_j] = 1
            cnt += 1
            i = n_i
            j = n_j
        else :
            d += 1
            if d == 4 :
                d = 0
    else :
        d += 1 
        if d == 4 :
            d = 0
if check :
    print(j+1, i + 1)
else :
    print(0)