import sys
input = sys.stdin.readline

def soluction(K, coin) :
    for i in coin :
        if K - i >= 0 :
            v, r = divmod(K, i)
            return v, r

if __name__ == "__main__":
    N, K = map(int, input().split(" "))
    coin = []
    for _ in range(N) :
        coin.append(int(input()))
    coin = sorted(coin, key= lambda x: -x)
    answer = 0
    while K > 0 :
        a, K = soluction(K, coin)
        answer += a
    print(answer)
    