
map = []
dices = [[-1,0,-1], [0,0,0], [-1,0,-1], [-1,0,-1]]
di_x = 1
di_y = 1
buf = []
N, M, x, y, K = (input().split(' '))
skip_buf = 1

N = int(N)
M = int(M)
x = int(x)
y = int(y)
K = int(K)

for i in range(N) :
    map.append([])
    buf = input().split(' ')
    print(buf)
    for k in range(M):
        map[i].append(int(buf[k]))
    buf =[]

def move_dices(where,di_x,di_y) :
    if where == 1 :
        if di_x == 1 and di_y !=2 :
            di_y += 1
        elif di_x == 1 and di_y ==2 :
            di_y = 0
        else:
            di_x = 1
            di_y = 2
        
    elif where == 2 :
        if di_x == 1 and di_y !=0 :
            di_y -= 1
        elif di_x == 1 and di_y ==0 :
            di_y = 2
        else:
            di_x = 1
            di_y = 0
    elif where == 3 :
        if di_x != 0 and di_y ==1 :
            di_x -= 1
        elif di_x == 0 and di_y ==1 :
            di_x = 3
        else:
            di_x = 0
            di_y = 1
    elif where == 4 :
        if di_x != 3 and di_y ==1 :
            di_x += 1
        elif di_x == 3 and di_y ==1 :
            di_x = 0
        else:
            di_x = 2
            di_y = 1

    return di_x,di_y

def move_map(move_to,x,y,skip_buf) :
    if move_to == 1 :
        skip_buf = 1
        y +=1
        if y >= M :
            y -=1
            skip_buf = -1
    elif move_to == 2:
        skip_buf = 1
        y -=1 
        if y < 0 :
            y+=1
            skip_buf = -1
    elif move_to == 3 :
        skip_buf = 1
        x -= 1 
        if x <0 :
            x += 1 
            skip_buf = 1
    elif move_to == 4 :
        skip_buf = 1 
        x += 1 
        if x >= N :
            x -=1
            skip_buf = -1
    return x, y, skip_buf

buf = input().split(' ')
for i in buf :
    a = int(i)
    x, y, skip_buf =  move_map(a,x,y,skip_buf)

    if skip_buf != -1 :
        di_x , di_y= move_dices(a,di_x,di_y)
        if map[x][y] != 0 :
            dices[di_x][di_y] = map[x][y]
            if di_x == 1 and di_y == 1 :
                print(dices[3][1])
            elif di_x == 3 and di_y == 1 :
                print(dices[1][1])
            elif di_x == 0 and di_y == 1 :
                print(dices[2][1])
            elif di_x == 2 and di_y == 1 :
                print(dices[0][1])
            elif di_x == 1 and di_y == 0 :
                print(dices[1][2])
            elif di_x == 1 and di_y == 2 :
                print(dices[1][0])
            
            map[x][y] = 0

        else :
            map[x][y] = dices[di_x][di_y]
            if di_x == 1 and di_y == 1 :
                print(dices[3][1])
            elif di_x == 3 and di_y == 1 :
                print(dices[1][1])
            elif di_x == 0 and di_y == 1 :
                print(dices[2][1])
            elif di_x == 2 and di_y == 1 :
                print(dices[0][1])
            elif di_x == 1 and di_y == 0 :
                print(dices[1][2])
            elif di_x == 1 and di_y == 2 :
                print(dices[1][0])        
