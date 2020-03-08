import math

N, M = map(int, input().split(" "))


def knifeCount(sausage, people) :
    if sausage>=people and sausage%people == 0 :
        return 0
    else :
        return people - math.gcd(sausage, people)



print(knifeCount(N,M))



    