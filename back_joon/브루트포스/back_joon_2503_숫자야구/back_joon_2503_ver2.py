import sys
input = sys.stdin.readline

if __name__ == "__main__":
    game = []
    N = int(input())
    for _ in range(N) :
        game.append(list(map(str, input().rstrip().split(" "))))
    
    answer = 0
    for i in range(123, 988) :
        temp = str(i)
        if "0" in temp :
            continue
        if temp[0] == temp[1] or temp[0] == temp[2] or temp[1] == temp[2] :
            continue
        flag = True
        for num, s, b in game :
            strike = 0
            ball = 0
            for x in range(3) :
                for y in range(3) :
                    if x == y and temp[x] == num[y] : strike += 1
                    if x != y and temp[x] == num[y] : ball += 1
            if strike != int(s) or ball != int(b) :
                flag = False
                break
        if flag :
            answer += 1
    
    print(answer)
                