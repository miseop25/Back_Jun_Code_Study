N, M = map(int, input().split(" "))


def knifeCount(sausage, people) :
    if sausage>=people and sausage%people == 0 :
        return 0

    cut = 1
    while True :
        cnt = cut*sausage
        piece = sausage*(cut+1)
        if piece%people == 0 :
            return cnt
        else :
            cut +=1

print(knifeCount(N,M))



    