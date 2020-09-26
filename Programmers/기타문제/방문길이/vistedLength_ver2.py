def solution(dirs):
    answer = 0
    x,y = 0,0
    cmdDict = {"U" : 0, "D":1,"R":2, "L":3}
    dy = [0,0,1,-1]
    dx = [-1,1,0,0]
    visted = set()

    for k in dirs :
        index = cmdDict[k]

        if x + dx[index] < -5 or x+ dx[index] > 5 or y + dy[index] < -5 or y + dy[index] > 5 :
            continue
        newX = x + dx[index]
        newY = y + dy[index]
        if (x,y,newX,newY) not in visted :
            visted.add((x,y,newX,newY))
            visted.add((newX,newY, x,y))
            answer += 1
        x = newX
        y = newY

    return answer


print(solution("UUUDDD"))