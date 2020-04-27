def fibo(a) :
    x1, x2 = 0, 1
    if a == 1 :
        return 1
    n = abs(a) 
    for _ in range(n) :
        x1, x2 = x2 , (x1 + x2 )%1000000000
    return x1



N = int(input())

if N == 0 :
    print(0)
    print(0)
elif N > 0 :
    print(1)
    print(fibo(N))
else :
    if abs(N)%2 == 0 :
        print(-1)
    else :
        print(1)
    print(fibo(N))


