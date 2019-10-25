def count_uphill(N) : 
    up_hill = 0
    if N == 1 : return 10
    max_range = 10**(N)
    sep = 10**(N-1)
    for i in range(max_range):
        if (int(i/sep) <=int(i%sep) ) :
            up_hill +=1


    return up_hill



N = int(input())
print(count_uphill(N))