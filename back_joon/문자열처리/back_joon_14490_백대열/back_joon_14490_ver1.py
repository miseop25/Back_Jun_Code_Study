from math import gcd

if __name__ == "__main__":
    n,m = map(int, input().split(":"))
    g = gcd(n,m)
    n = n//g
    m = m//g
    answer = str(n) + ":" + str(m)
    print(answer)