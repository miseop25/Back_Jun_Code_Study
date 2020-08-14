import sys
input = sys.stdin.readline

if __name__ == "__main__":
    numList = [True]*1000
    N = int(input())
    for _ in range(N) :
        num, s, b = map(str, input().rstrip().split(" "))
        for i in range(1000) :
            temp = str(i)
            strike = 0
            ball = 0
            if i<123 :
                numList[i] = False
                continue
            if temp[0] == temp[1] or temp[1] == temp[2] or temp[0] == temp[2] :
                numList[i] = False
                continue
            if "0" in temp :
                numList[i] = False
                continue

            for j in range(3) :
                if num[j] == temp[j] :
                    strike += 1
                elif num[j] in temp :
                    ball += 1
            if int(s) == strike and int(b) == ball :
                numList[i] = True
            else :
                numList[i] = False
    
    answer = 0
    for i in numList :
        if i :
            answer += 1
    print(answer)
                

                    
    