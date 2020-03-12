import sys
input = sys.stdin.readline

M ,N = map(int, input().split(" "))
tomato = []
day = 0
for i in range(N) :
    buf = list(map(int, input().split(" ")))
    tomato.append(buf)

def change_tomato(tomato, M, N) :
    changed_list = []
    for i in range(N) :
        for j in range(M) :
            if tomato[i][j] == 1 :
                #우측으로 익는 것
                if j != (M-1) :
                    if tomato[i][j+1] != -1 and tomato[i][j+1] != 1 :
                        changed_list.append([i,j+1])
                #좌측으로 익는 것
                if j != 0 :
                    if tomato[i][j-1] != -1 and tomato[i][j-1] != 1 :
                        changed_list.append([i, j-1])
                #위 쪽으로 익는 것
                if i != 0 :
                    if tomato[i-1][j] != -1 and tomato[i-1][j] != 1 :
                        changed_list.append([i-1, j])
                # 아래쪽으로 익는 것
                if i != (N-1) :
                    if tomato[i+1][j] != -1 and tomato[i+1][j] != 1 :
                        changed_list.append([i+1, j])
    if changed_list :
        return changed_list
    else :
        return -1

def update_tomato(update_list, tomato) :
    for i in update_list :
        tomato[i[0]][i[1]] = 1
    return tomato


while True :
    tmep_list = change_tomato(tomato, M, N)
    if tmep_list != -1 :
        tomato = update_tomato(tmep_list, tomato)
        day += 1 
    else :
        break

for i in range(N) :
    if 0 in tomato[i] :
        day = -1
        break
    
print(day)
