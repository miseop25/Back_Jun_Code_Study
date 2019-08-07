import sys

N = int(input())


while N>0 :
    west_point, east_point = (input().split())
    K = int(west_point)
    w_prod = 1
    e_prod = 1


    while K >0:
        w_prod = w_prod*(int(east_point)-K+1)
        e_prod = e_prod*K
        K = K-1

    output = round(w_prod/e_prod)
    print(output)


    N = N-1
