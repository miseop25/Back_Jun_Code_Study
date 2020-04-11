def soluction(N) :
    count = [1,1]
    if N <= 2 :
        return 1
    for i in range(2, N) :
        count.append(count[i-1] + count[i-2])
    return count[-1]
N = int(input())
print(soluction(N))