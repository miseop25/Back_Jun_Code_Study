import sys
input = sys.stdin.readline

def soluction(N,K, num) :

    cnt = 0
    i =
    for i in range(1,N) :
        if num[i-1] <= num[i] :
            num[i-1] = ''
            cnt += 1
    
        if cnt == K :
            break
    i = N-1
    while cnt != K :
        if num[i] != '' :
            num[i] = ''
            i -= 1
            cnt += 1

    return ''.join(num)



if __name__ == "__main__":
    N, K = map(int, input().split(" "))
    num = list(input().rstrip())
    print(soluction(N,K,num))


